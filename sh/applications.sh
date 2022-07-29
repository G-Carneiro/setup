#!/bin/bash

# Manually install
# bitwarden   https://bitwarden.com/download/
# toolbox     https://www.jetbrains.com/toolbox-app/
# pandoc      https://github.com/jgm/pandoc/releases/latest
# pcloud      https://www.pcloud.com/download-free-online-cloud-file-storage.html

# This install all applications I need in post install linux distribution based in debian.
# FIXME: bitwarden, toolbox, pandoc and pcloud release auto update apt
#  or oficial flatpak support or generic link download (agnostic version).

# Variables
apps_dir="$HOME/Downloads/Applications"
python_version=python3.9

ppas=(
 tatokis/ckb-next
 lutris-team/lutris
)

declare -A deb_to_url

deb_to_url=(
  [discord]="https://discord.com/api/download?platform=linux&format=deb"
  [mailspring]="https://updates.getmailspring.com/download?platform=linuxDeb"
  [google_chrome]="https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
  [freedownloadmanager]="https://dn3.freedownloadmanager.org/6/latest/freedownloadmanager.deb"
)

apt_packages=(
  apt-transport-https   # required for brave-browser
  curl                  # required for brave-browser
  git
  whatsapp-desktop      # wait official support
  grub-customizer
  gnome-clocks
  texlive-full
  shellcheck
  spotify-client
  pdf2svg
  "$python_version"-full
  "$python_version"-dev
  "$python_version"-dbg
  python3-tk-dbg
  python3-pip
  brave-browser
  anydesk
  ckb-next              # only desktop
  # pympress dependencies
  pympress
  libgtk-3-0
  libpoppler-glib8
  libcairo2
  python3-gi
  python3-gi-cairo
  gobject-introspection
  libgirepository-1.0-1
  gir1.2-gtk-3.0
  gir1.2-poppler-0.18
)

# TODO: change to dict
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

remove_apt=(
  sticky                  # notes
  thunderbird             # email manager
  firefox
  firefox-locale-en
  firefox-locale-pt
  hexchat-common
  libreoffice-common
  idle-"$python_version"
)

# Brave Browser requirements
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
for program in "${flatpak_packages[@]}"; do
  flatpak install flathub "$program" -y
  echo "[Installed] - $program"
done

# Download files from URL's and install
for key in "${!deb_to_url[@]}"; do
  wget -q -O "$apps_dir/$key".deb -c "${deb_to_url[$key]}"
  echo "[Downloaded] - $key"
done

sudo dpkg -i "$apps_dir/*.deb"

for file in "$apps_dir"/*.tar.gz; do
  tar -xzvf "$file";
done

for program in "${remove_apt[@]}"; do
  sudo apt remove "$program" -y
  echo "[Removed] - $program"
done

# Clean, update and upgrade
pip install --upgrade pip
pip install jupyter
sudo apt update && sudo apt dist-upgrade -y
flatpak update
sudo apt autoclean
sudo apt autoremove -y

## Final message ##
echo "All installations have been completed!"
