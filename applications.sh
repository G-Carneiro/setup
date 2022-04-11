#!/bin/bash

# Repository programs

# bash -c "$(wget -q -O - https://linux.kite.com/dls/linux/current)"

	# Browser requirements

sudo apt install apt-transport-https curl -y

sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg -y

echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list

	# PPAs

sudo add-apt-repository ppa:apandada1/xournalpp-stable -y

sudo add-apt-repository ppa:inkscape.dev/stable -y

sudo add-apt-repository ppa:tatokis/ckb-next-git -y

	## Installation

sudo apt update -y

sudo apt install git -y

sudo apt install python3-pip -y

sudo apt install python3.8-venv -y

sudo apt install python3.8-tk -y

sudo apt install whatsapp-desktop -y

sudo apt install neovim -y

sudo apt install flameshot -y

sudo apt install gnome-clocks -y

sudo apt install texlive-full -y

sudo apt install pandoc -y

sudo apt install shellcheck -y

sudo apt install discord -y

sudo apt install mailspring -y

sudo apt install spotify-client -y

sudo apt install bitwarden -y

sudo apt install pdf2svg -y

sudo apt install brave-browser -y

sudo apt install xournalpp -y

sudo apt install inkscape -y

sudo apt install ckb-next -y

sudo apt update -y

pip install --upgrade pip

pip install Jupyter

# Flatpaks

flatpak install flathub org.telegram.desktop -y

flatpak install flathub com.github.debauchee.barrier -y

flatpak install flathub com.obsproject.Studio -y

flatpak install flathub org.kde.kdenlive -y

flatpak install flathub io.github.lainsce.Colorway -y

flatpak install flathub io.github.lainsce.Emulsion -y

## Final mensage ##

echo "All installations have been completed!"
