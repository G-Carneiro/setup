#!/bin/bash

# Variables

apps_dir="$HOME/Downloads/Applications"

ppas=(
 "inkscape.dev/stable"
 "tatokis/ckb-next"
)

urls=(
  "https://www.pcloud.com/how-to-install-pcloud-drive-linux.html?download=electron-64"
  "https://vault.bitwarden.com/download/?app=desktop&platform=linux&variant=deb"
  "https://vault.bitwarden.com/download/?app=desktop&platform=linux&variant=deb"
)
url_droidcam="https://files.dev47apps.net/linux/droidcam_1.8.2.zip"

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
  google-chrome-stable
)

flatpak_packages=(
  io.neovim.nvim
  org.telegram.desktop
  org.flameshot.Flameshot
  com.github.debauchee.barrier
  com.github.xournalpp.xournalpp
  io.github.lainsce.Colorway
  io.github.lainsce.Emulsion
  org.kde.kdenlive
  com.obsproject.Studio
)

cd "$apps_dir" || exit

	# Browser requirements

sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg -y

echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list

	# PPAs

for apt_repository in "${ppas[@]}"; do
  sudo add-apt-repository "ppa:$apt_repository"
  echo "[Added] $apt_repository"
done

	## Installation

sudo apt update -y

# TODO: change python version and install all about python
sudo apt install python3-pip -y

sudo apt install python3.8-venv -y

sudo apt install python3.8-tk -y

sudo apt install bitwarden -y

sudo apt install brave-browser -y

sudo apt install inkscape -y

sudo apt install ckb-next -y

sudo apt update -y

pip install --upgrade pip

# Install apt packages

for program in "${apt_packages[@]}"; do
  apt install "$program" -y
  echo "[Installed] - $program"
done

# Install Flatpak packages

for program in "${flatpak_packages[@]}"; do
  flatpak install flathub "$program" -y
  echo "[Installed] - $program"
done

## Final message ##

echo "All installations have been completed!"
