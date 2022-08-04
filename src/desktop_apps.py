from typing import Dict, List

# TODO: check steamcmd
# TODO: find multiseat solution (like aster for windows https://www.asterpro.com.br/)
# TODO: find solution to gamepad
desktop_ppas: List[str] = [
    "flexiondotorg/mangohud",
    "tatokis/ckb-next"
]

desktop_deb_to_url: Dict[str, str] = {}

desktop_apt_packages: List[str] = [
    "ckb-next",
    "goverlay",
    "lutris",
    "steam"
]

desktop_flatpak_packages: Dict[str, str] = {
    "AntiMicroX": "io.github.antimicrox.antimicrox",    # official support
    "Citra": "org.citra_emu.citra",                     # official support
    "Kdenlive": "org.kde.kdenlive",                     # official support
    "obs-studio": "com.obsproject.Studio",              # official support
    "RetroArch": "org.libretro.RetroArch"               # official support
}

desktop_remove_apt_packages: List[str] = []
