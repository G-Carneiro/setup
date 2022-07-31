#!/bin/bash

# Manually install
# bitwarden   https://bitwarden.com/download/
# toolbox     https://www.jetbrains.com/toolbox-app/
# pandoc      https://github.com/jgm/pandoc/releases/latest
# pcloud      https://www.pcloud.com/download-free-online-cloud-file-storage.html

# This install all applications I need in post install linux distribution based in debian.
# FIXME: wait brave-browser, anydesk, bitwarden, toolbox, pandoc and pcloud
#  release auto update apt or oficial flatpak support or generic link download (agnostic version).
# TODO: install pympress by default or not? https://github.com/Cimbali/pympress/

# Variables
python_version=python3.9
apps_dir="$HOME/Downloads/Applications"
deb_dir="$apps_dir/deb"
appImage_dir="$apps_dir/AppImage"

ppas=()

declare -A deb_to_url
deb_to_url=(
  [discord]="https://discord.com/api/download?platform=linux&format=deb"
  [mailspring]="https://updates.getmailspring.com/download?platform=linuxDeb"
  [google_chrome]="https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
  [freedownloadmanager]="https://dn3.freedownloadmanager.org/6/latest/freedownloadmanager.deb"
)

apt_packages=(
  anydesk
  brave-browser
  git
  gnome-clocks
  grub-customizer
  pdf2svg
  "$python_version"-dev
  "$python_version"-dbg
  "$python_version"-full
  python3-pip
  python3-tk-dbg
  shellcheck
  spotify-client
  texlive-full
  whatsapp-desktop        # wait official support
)

declare -A flatpak_packages
flatpak_packages=(
  [barrier]=com.github.debauchee.barrier      # official support
  [colorway]=io.github.lainsce.Colorway       # official support
  [emulsion]=io.github.lainsce.Emulsion       # official support
  [flameshot]=org.flameshot.Flameshot         # official support
  [inkscape]=org.inkscape.Inkscape            # official support
  [neovim]=io.neovim.nvim                     # official support
  [telegram]=org.telegram.desktop             # official support
  [xournalpp]=com.github.xournalpp.xournalpp  # official support
)

remove_apt=(
  firefox
  firefox-locale-en
  firefox-locale-pt
  hexchat-common
  idle-"$python_version"
  libreoffice-common
  sticky                  # notes
  thunderbird             # email manager
)

# Brave Browser requirements
sudo apt install apt-transport-https curl -y
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg -y
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list

# AnyDesk requirements
wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | apt-key add -
echo "deb http://deb.anydesk.com/ all main" > /etc/apt/sources.list.d/anydesk-stable.list

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
  file="${deb_dir}/${key}.deb"
  wget -q -O "$file" -c "${deb_to_url[$key]}"
  sudo dpkg -i "$file"
  echo "[Installed] - $key"
done

for program in "${remove_apt[@]}"; do
  sudo apt remove "$program" -y
  echo "[Removed] - $program"
done

pip install --upgrade pip
pip install jupyter

# Clean, update and upgrade
sudo apt update && sudo apt dist-upgrade -y
flatpak update
sudo apt autoclean
sudo apt autoremove -y

## Final message ##
echo "All installations have been completed!"
