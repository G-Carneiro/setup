#!/bin/bash

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

bash ./general
bash ./appications "${ppas[@]}" "${apt_packages[@]}" "${!flatpak_packages[@]}" "${!deb_to_url[@]}" "${remove_apt[@]}"
bash ./droidcam