from typing import Dict, List

from .Symlink import Symlink
from .global_variables import *
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


def _update_symlinks(symlinks: Dict[str, Symlink]) -> None:
    symlinks.update({
        "gtk-3.0": Symlink(name="gtk-3.0", origin=f"{DESKTOP_CONFIG}", destiny=f"{CONFIG}", file="bookmarks"),
        "transmission": Symlink(name="transmission", origin=f"{DESKTOP_CONFIG}", destiny=f"{CONFIG}",
                                file="settings.json")
    })
    return None


def _update_copy_files(copy_files: Dict[str, Symlink]) -> None:
    copy_files.update({
        "discord": Symlink(name="discord", origin=f"{DESKTOP_CONFIG}", destiny=f"{CONFIG}", file="settings.json"),
        "whatsapp-conf": Symlink(name="whatsapp", origin=f"{DESKTOP_CONFIG}", destiny=f"{VAR_APP}", file="config.json")
    })
    return None


def _update_icons(icons: Dict[str, str]) -> None:
    icons.update({
        f"{ANIMES}": f"{IMG}/crunchyroll.svg",
        f"{ANIMES}/One\\ Piece": f"{ANIMES_ICON}/one-piece.png",
        f"{ANIMES}/One\\ Piece/One\\ Piece\\ EX\\ -\\ 1\\ East\\ Blue":
            f"{ANIMES_ICON}/One_Piece/arlong.png",
        f"{ANIMES}/One\\ Piece/One\\ Piece\\ EX\\ -\\ 2\\ Baroque\\ Works":
            f"{ANIMES_ICON}/One_Piece/baroque-works.png",
        f"{ANIMES}/One\\ Piece/One\\ Piece\\ EX\\ -\\ 3\\ Skypiea":
            f"{ANIMES_ICON}/One_Piece/enel.png",
        f"{ANIMES}/One\\ Piece/One\\ Piece\\ EX\\ -\\ 4\\ Water\\ 7\\ ~\\ CP9":
            f"{ANIMES_ICON}/One_Piece/world-government.png",
        f"{ANIMES}/One\\ Piece/One\\ Piece\\ EX\\ -\\ 5\\ Thriller\\ Bark":
            f"{ANIMES_ICON}/One_Piece/thriller-bark.png",
        f"{ANIMES}/One\\ Piece/One\\ Piece\\ EX\\ -\\ 6\\ Arquipélago\\ Sabaody":
            f"{ANIMES_ICON}/One_Piece/kuja-pirates.png",
        f"{ANIMES}/One\\ Piece/One\\ Piece\\ EX\\ -\\ 7\\ Impel\\ Down":
            f"{ANIMES_ICON}/One_Piece/spade-pirates.png",
        f"{ANIMES}/One\\ Piece/One\\ Piece\\ EX\\ -\\ 8\\ Marineford":
            f"{ANIMES_ICON}/One_Piece/whitebeard.png",
        f"{ANIMES}/One\\ Piece/One\\ Piece\\ EX\\ -\\ 9\\ Pós\\ Guerra":
            f"{ANIMES_ICON}/One_Piece/straw-hat.png",
        f"{ANIMES}/One\\ Piece/One\\ Piece\\ EX\\ -\\ 10\\ Ilha\\ dos\\ Tritões":
            f"{ANIMES_ICON}/One_Piece/sun-pirates.png",
        f"{ANIMES}/One\\ Piece/One\\ Piece\\ EX\\ -\\ 11\\ Punk\\ Hazard":
            f"{ANIMES_ICON}/One_Piece/heart-pirates.png",
        f"{ANIMES}/One\\ Piece/One\\ Piece\\ EX\\ -\\ 12\\ Dressrosa":
            f"{ANIMES_ICON}/One_Piece/doflamingo.png",
        f"{ANIMES}/One\\ Piece/One\\ Piece\\ EX\\ -\\ 13\\ Zou":
            f"{ANIMES_ICON}/One_Piece/zunesha.png",
        f"{ANIMES}/One\\ Piece/One\\ Piece\\ EX\\ -\\ 14\\ Whole\\ Cake":
            f"{ANIMES_ICON}/One_Piece/big-mom.png",
        f"{ANIMES}/One\\ Piece/One\\ Piece\\ EX\\ -\\ 15\\ Wano":
            f"{ANIMES_ICON}/One_Piece/kaido.png",
        f"{ANIMES}/Alderamin\\ on\\ The\\ Sky":
            f"{ANIMES_ICON}/alderamin-on-the-sky.png",
        f"{ANIMES}/Go-toubun":
            f"{ANIMES_ICON}/go-toubun.png",
        f"{ANIMES}/Haikyuu":
            f"{ANIMES_ICON}/haikyuu.png",
        f"{ANIMES}/Jujutsu\\ Kaisen":
            f"{ANIMES_ICON}/jujutsu-kaisen.png",
        f"{ANIMES}/Kimetsu\\ no\\ Yaiba":
            f"{ANIMES_ICON}/kimetsu.png",
        f"{ANIMES}/Kimi\\ no\\ Uso":
            f"{ANIMES_ICON}/kimi-no-uso.png",
        f"{ANIMES}/One\\ Punch\\ Man":
            f"{ANIMES_ICON}/one-punch-man.png",
        f"{ANIMES}/ReZero":
            f"{ANIMES_ICON}/rezero.png",
        f"{ANIMES}/Sword\\ Art\\ Online":
            f"{ANIMES_ICON}/sao.png",
        f"{CCO}": f"{IMG}/monitor.png",
    })
    return None


def update_all_packages(ppas: List[str],
                        deb: Dict[str, str],
                        apt_packages: List[str],
                        remove_apt_packages: List[str],
                        flatpak_packages: Dict[str, str],
                        symlinks: Dict[str, Symlink]
                        ) -> None:
    _update_deb(deb=deb)
    _update_ppas(ppas=ppas)
    _update_apt(apt_packages=apt_packages)
    _update_flatpak_packages(flatpak_packages=flatpak_packages)
    _update_remove_apt_packages(remove_apt_packages=remove_apt_packages)
    _update_symlinks(symlinks=symlinks)
    return None
