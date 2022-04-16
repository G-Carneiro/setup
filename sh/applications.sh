#!/bin/bash

# This install all applications I need in post install linux distribution based in debian.
# FIXME: wait mailspring, bitwarden, toolbox and pcloud release auto update apt
#  or oficial flatpak support or generic link download (agnostic version).

# Variables
apps_dir="$HOME/Downloads/Applications"

ppas=(
 "tatokis/ckb-next"
)

urls=(
  "https://dn3.freedownloadmanager.org/6/latest/freedownloadmanager.deb"
  "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
  "https://download.jetbrains.com/toolbox/jetbrains-toolbox-1.23.11731.tar.gz"
)

apt_packages=(
  apt-transport-https   # required for brave-browser
  curl                  # required for brave-browser
  git
  whatsapp-desktop
  gnome-clocks
  texlive-full
  shellcheck
  discord
  spotify-client
  pdf2svg
  python3.9-full
  python3.9-dev
  python3.9-dbg
  python3-tk-dbg
  python3-pip
  brave-browser
  ckb-next              # only desktop
)

flatpak_packages=(
  io.neovim.nvim
  org.telegram.desktop
  org.inkscape.Inkscape
  org.flameshot.Flameshot
  com.github.debauchee.barrier
  com.github.xournalpp.xournalpp
  io.github.lainsce.Colorway
  io.github.lainsce.Emulsion
  org.kde.kdenlive                  # only desktop
  com.obsproject.Studio             # only desktop
)

# Brave Browser requirements
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg -y

echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list

# Add third party packages - PPAs
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

# Download files from URL's and install
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
