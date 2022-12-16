from os import scandir
from typing import Dict, List

from .Symlink import Symlink
from .global_variables import *


# TODO: mount disks (/etc/fstab)
# TODO: check steamcmd
# TODO: find multiseat solution (like aster for windows https://www.asterpro.com.br/)
# TODO: find solution to gamepad
# https://www.edrawsoft.com/edraw-max/


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
        "steam"
    ]
    return None


def _update_flatpak_packages(flatpak_packages: Dict[str, str]) -> None:
    flatpak_packages.update({
        "AntiMicroX": "io.github.antimicrox.antimicrox",    # official support
        "Citra": "org.citra_emu.citra",                     # official support
        # "Kdenlive": "org.kde.kdenlive",                     # official support
        "Lutris": "net.lutris.Lutris",                      # official support
        # "obs-studio": "com.obsproject.Studio",              # official support
        "RetroArch": "org.libretro.RetroArch",              # official support
        "UserModeFTP": "eu.ithz.umftpd",                    # official support
    })
    return None


def _update_remove_apt_packages(remove_apt_packages: List[str]) -> None:
    remove_apt_packages += []
    return None


def _update_symlinks(symlinks: Dict[str, Symlink]) -> None:
    symlinks.update({
        "gtk-3.0": Symlink(name="gtk-3.0", origin=f"{DESKTOP_CONFIG}", destiny=f"{CONFIG}", file="bookmarks"),
        "transmission": Symlink(name="transmission", origin=f"{DESKTOP_CONFIG}", destiny=f"{CONFIG}",
                                file="settings.json"),
        "animes": Symlink(name="Animes", origin=f"{MNT}", destiny=f"{HOME}", file="Animes"),
        "cco": Symlink(name="Others", origin=f"{MNT}", destiny=f"{HOME}", file="CCO"),
        "series": Symlink(name="Others", origin=f"{MNT}", destiny=f"{HOME}", file="Series")
    })
    return None


def _update_copy_files(copy_files: Dict[str, Symlink]) -> None:
    copy_files.update({
        "discord": Symlink(name="discord", origin=f"{DESKTOP_CONFIG}", destiny=f"{CONFIG}", file="settings.json"),
        "whatsapp-conf": Symlink(name="whatsapp", origin=f"{DESKTOP_CONFIG}", destiny=f"{VAR_APP}", file="config.json")
    })
    return None


def _update_icons(icons: Dict[str, str], icons_dir: str = f"{ICONS}",
                  target_dir: str = f"{HOME}") -> None:
    for archive in scandir(icons_dir):
        archive_name: str = archive.name
        for target_file in scandir(target_dir):
            target_name: str = target_file.name
            if target_file.is_dir() \
                    and (archive_name.lower().replace(" ", "-")[:-4] in target_name.lower().replace(" ", "-")):
                if archive.is_file():
                    target_path = target_file.path
                    archive_path = archive.path
                    icons[target_path] = archive_path
                else:
                    _update_icons(icons=icons, icons_dir=archive.path, target_dir=target_file.path)
                break
    return None


def _update_mkdir(mkdir: List[str]) -> None:
    mkdir += []
    return None


def _update_dconf(dconf: Dict[str, str]) -> None:
    dconf.update({})
    return None


def update_all_packages(ppas: List[str],
                        deb: Dict[str, str],
                        apt_packages: List[str],
                        remove_apt_packages: List[str],
                        flatpak_packages: Dict[str, str],
                        symlinks: Dict[str, Symlink],
                        icons: Dict[str, str],
                        mkdir: List[str],
                        dconf: Dict[str, str]
                        ) -> None:
    _update_deb(deb=deb)
    _update_ppas(ppas=ppas)
    _update_apt(apt_packages=apt_packages)
    _update_flatpak_packages(flatpak_packages=flatpak_packages)
    _update_remove_apt_packages(remove_apt_packages=remove_apt_packages)
    _update_symlinks(symlinks=symlinks)
    _update_icons(icons=icons)
    _update_mkdir(mkdir=mkdir)
    _update_dconf(dconf=dconf)
    return None
