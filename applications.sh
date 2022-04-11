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

sudo apt-get update -y

sudo apt-get install git -y

sudo apt-get install python3-pip -y

sudo apt-get install python3.8-venv -y

sudo apt-get install python3.8-tk -y

sudo apt-get install whatsapp-desktop -y

sudo apt-get install neovim -y

sudo apt-get install flameshot -y

sudo apt-get install gnome-clocks -y

sudo apt-get install texlive-full -y

sudo apt-get install pandoc -y

sudo apt-get install shellcheck -y

sudo apt-get install spotify-client -y

sudo apt-get install pdf2svg -y

sudo apt-get install brave-browser -y

sudo apt-get install xournalpp -y

sudo apt-get install inkscape -y

sudo apt-get install ckb-next -y

sudo apt-get update -y

pip install --upgrade pip

pip install Jupyter

# Flatpaks

flatpak install flathub org.telegram.desktop -y

flatpak install flathub com.discordapp.Discord -y
# https://discord.com/api/download?platform=linux&format=deb

flatpak install flathub com.github.debauchee.barrier -y

flatpak install flathub com.jetbrains.PyCharm-Professional -y

flatpak install flathub com.jetbrains.CLion -y

flatpak install flathub com.obsproject.Studio -y

flatpak install flathub org.kde.kdenlive -y

flatpak install flathub io.github.lainsce.Colorway -y

flatpak install flathub io.github.lainsce.Emulsion -y

flatpak install flathub com.getmailspring.Mailspring -y # change to .deb
# https://updates.getmailspring.com/download?platform=linuxDeb

# TODO: https://bitwarden.com/download/
# https://vault.bitwarden.com/download/?app=desktop&platform=linux&variant=deb

## Final mensage ##

echo "All installations have been completed!"
