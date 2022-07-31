#!/bin/bash

# Variables
apps_dir="$HOME/Downloads/Applications"
deb_dir="$apps_dir/deb"
appImage_dir="$apps_dir/AppImage"

ppas=(
 tatokis/ckb-next
 lutris-team/lutris
)

declare -A deb_to_url
deb_to_url=()

apt_packages=(
  ckb-next
  lutris
)

declare -A flatpak_packages
flatpak_packages=(
  [kdenlive]=org.kde.kdenlive                 # official support
  [obs-studio]=com.obsproject.Studio          # official support
)

remove_apt=()

# Add third party packages - PPAs
sudo apt update -y

for apt_repository in "${ppas[@]}"; do
  sudo add-apt-repository "ppa:$apt_repository"
  echo "[Added] - $apt_repository"
done

# Install apt packages
sudo apt update -y

for program in "${apt_packages[@]}"; do
  sudo apt install "$program" -y
  echo "[Installed] - $program"
done

# Install Flatpak packages
for program in "${!flatpak_packages[@]}"; do
  flatpak install flathub "${flatpak_packages[program]}" -y
  echo "[Installed] - $program"
done

# Download files from URL's and install
for key in "${!deb_to_url[@]}"; do
  file="${deb_dir}/${key}.deb"
  wget -q -O "$file" -c "${deb_to_url[$key]}"
  sudo dpkg -i "$file"
  echo "[Installed] - $key"
done

for program in "${remove_apt[@]}"; do
  sudo apt remove "$program" -y
  echo "[Removed] - $program"
done

# Clean, update and upgrade
sudo apt update && sudo apt dist-upgrade -y
flatpak update
sudo apt autoclean
sudo apt autoremove -y

## Final message ##
echo "All installations have been completed!"

bash ./general
bash ./droidcam