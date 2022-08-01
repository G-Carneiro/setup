from typing import Dict, List

# TODO: check steamcmd
# TODO: find multiseat solution (like aster for windows https://www.asterpro.com.br/)
ppas: List[str] = [
    "tatokis/ckb-next"
]

deb_to_url: Dict[str, str] = {}

apt_packages: List[str] = [
    "ckb-next",
    "lutris",
    "steam"
]

flatpak_packages: Dict[str, str] = {
    "kdenlive": "org.kde.kdenlive",         # official support
    "obs-studio": "com.obsproject.Studio"   # official support
}

remove_apt: List[str] = []
