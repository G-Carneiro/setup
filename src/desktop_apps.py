from typing import Dict, List

# TODO: check steamcmd
# TODO: find multiseat solution (like aster for windows https://www.asterpro.com.br/)
# TODO: find solution to gamepad
ppas: List[str] = [
    "flexiondotorg/mangohud",
    "tatokis/ckb-next"
]

deb_to_url: Dict[str, str] = {}

apt_packages: List[str] = [
    "ckb-next",
    "goverlay",
    "lutris",
    "steam"
]

flatpak_packages: Dict[str, str] = {
    "AntiMicroX": "io.github.antimicrox.antimicrox",    # official support
    "Citra": "org.citra_emu.citra",                     # official support
    "Kdenlive": "org.kde.kdenlive",                     # official support
    "obs-studio": "com.obsproject.Studio",              # official support
    "RetroArch": "org.libretro.RetroArch"               # official support
}

remove_apt: List[str] = []
