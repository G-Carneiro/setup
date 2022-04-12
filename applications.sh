#!/bin/bash

# Variables

ppa_inkscape="ppa:inkscape.dev/stable"
ppa_ckb="ppa:tatokis/ckb-next"

url_pcloud="https://www.pcloud.com/how-to-install-pcloud-drive-linux.html?download=electron-64"
url_bitwarden="https://vault.bitwarden.com/download/?app=desktop&platform=linux&variant=deb"
url_toolbox="https://download.jetbrains.com/toolbox/jetbrains-toolbox-1.23.11731.tar.gz"
url_droidcam="https://files.dev47apps.net/linux/droidcam_1.8.2.zip"

apps_dir="$HOME/Downloads/Applications"

apt_packages=(
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

sudo apt install apt-transport-https curl -y

sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg -y

echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list

	# PPAs

sudo add-apt-repository ppa:inkscape.dev/stable -y

sudo add-apt-repository ppa:tatokis/ckb-next -y

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

# Flatpaks

## Final message ##

echo "All installations have been completed!"
