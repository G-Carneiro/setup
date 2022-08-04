from typing import Dict, List

# TODO: check steamcmd
# TODO: find multiseat solution (like aster for windows https://www.asterpro.com.br/)
# TODO: find solution to gamepad


def _update_ppas(ppas: List[str]) -> None:
    ppas += [
        "flexiondotorg/mangohud",
        "tatokis/ckb-next"
    ]
    return None


def _update_deb(deb: Dict[str, str]) -> None:
    deb.update({
    })
    return None


def _update_apt(apt_packages: List[str]) -> None:
    apt_packages += [
        "ckb-next",
        "goverlay",
        "lutris",
        "steam"
    ]
    return None


def _update_flatpak_packages(flatpak_packages: Dict[str, str]) -> None:
    flatpak_packages.update({
        "AntiMicroX": "io.github.antimicrox.antimicrox",    # official support
        "Citra": "org.citra_emu.citra",                     # official support
        "Kdenlive": "org.kde.kdenlive",                     # official support
        "obs-studio": "com.obsproject.Studio",              # official support
        "RetroArch": "org.libretro.RetroArch"               # official support
    })
    return None


def _update_remove_apt_packages(remove_apt_packages: List[str]) -> None:
    remove_apt_packages += []
    return None


def update_all_packages(ppas: List[str],
                        deb: Dict[str, str],
                        apt_packages: List[str],
                        remove_apt_packages: List[str],
                        flatpak_packages: Dict[str, str]
                        ) -> None:
    _update_deb(deb=deb)
    _update_ppas(ppas=ppas)
    _update_apt(apt_packages=apt_packages)
    _update_flatpak_packages(flatpak_packages=flatpak_packages)
    _update_remove_apt_packages(remove_apt_packages=remove_apt_packages)
    return None
