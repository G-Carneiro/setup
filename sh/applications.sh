#!/bin/bash

# Variables
ppas=${1:-()}
apt_packages=${2:-()}
flatpak_packages=${3:-()}
deb_to_url=${4:-()}
remove_apt=${5:-()}

apps_dir="$HOME/Downloads/Applications"
deb_dir="$apps_dir/deb"
appImage_dir="$apps_dir/AppImage"

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
mkdir "$apps_dir" "$deb_dir" "$appImage_dir"
for key in "${!deb_to_url[@]}"; do
  wget -q -O "$deb_dir/$key".deb -c "${deb_to_url[$key]}"
  echo "[Downloaded] - $key"
done

sudo dpkg -i "$deb_dir/*.deb"

for file in "$apps_dir"/*.tar.gz; do
  tar -xzvf "$file";
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
