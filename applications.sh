#!/bin/bash

# Variables

apps_dir="$HOME/Downloads/Applications"

ppas=(
 "inkscape.dev/stable"
 "tatokis/ckb-next"
)

urls=(
  "https://download.jetbrains.com/toolbox/jetbrains-toolbox-1.23.11731.tar.gz"
)
  # TODO: extract tar.gz

apt_packages=(
  apt-transport-https   # required for brave-browser
  curl                  # required for brave-browser
  git
  whatsapp-desktop
  gnome-clocks
  texlive-full
  shellcheck
  discord
  mailspring
  spotify-client
  pdf2svg
  freedownloadmanager
  python3.9-full
  python3.9-dev
  python3.9-dbg
  python3-tk-dbg
  python3-pip
  google-chrome-stable
  bitwarden
  brave-browser
  inkscape
  ckb-next              # only desktop
)

flatpak_packages=(
  io.neovim.nvim
  org.telegram.desktop
  org.flameshot.Flameshot
  com.github.debauchee.barrier
  com.github.xournalpp.xournalpp
  io.github.lainsce.Colorway
  io.github.lainsce.Emulsion
  org.kde.kdenlive                  # only desktop
  com.obsproject.Studio             # only desktop
)

	# Browser requirements

sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg -y

echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list

	# PPAs

sudo apt update -y

for apt_repository in "${ppas[@]}"; do
  sudo add-apt-repository "ppa:$apt_repository"
  echo "[Added] $apt_repository"
done

# Install apt packages

sudo apt update -y

for program in "${apt_packages[@]}"; do
  sudo apt install "$program" -y
  echo "[Installed] - $program"
done

# Install Flatpak packages

for program in "${flatpak_packages[@]}"; do
  flatpak install flathub "$program" -y
  echo "[Installed] - $program"
done

# URL's
for url in "${urls[@]}"; do
  wget -c "$url" -P "$apps_dir"
done

sudo dpkg -i "$apps_dir/*.deb"

for file in "$apps_dir"/*.tar.gz; do
  tar -xzvf "$file";
done

# Clean, update and upgrade

pip install --upgrade pip
sudo apt update && sudo apt dist-upgrade -y
flatpak update
sudo apt autoclean
sudo apt autoremove -y

## Final message ##

echo "All installations have been completed!"
