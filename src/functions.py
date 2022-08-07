from os import system
from typing import List, Dict


# TODO: bookmarks, mount disks (/etc/fstab), change directories icons, mkdir
from .Symlink import Symlink
from .global_variables import *


def add_apt_repository(programs: List[str]) -> None:
    for program in programs:
        system(f"sudo add-apt-repository ppa:{program} \n"
               f"echo [Added] - {program}")

    return None


def remove_apt(programs: List[str]) -> None:
    for program in programs:
        system(f"sudo apt remove {program} -y \n"
               f"echo [Removed] - {program}")

    return None


def install_flatpaks(programs: Dict[str, str]) -> None:
    for program, flatpak in programs.items():
        system(f"flatpak install flathub {flatpak} -y \n"
               f"echo [Installed] - {program}")

    return None


def install_apt(programs: List[str]) -> None:
    for program in programs:
        system(f"sudo apt install {program} -y \n"
               f"echo [Installed] - {program}")

    return None


def install_deb(programs: Dict[str, str]) -> None:
    for program, url in programs.items():
        file: str = f"{DEB_DIRECTORY}/{program}.deb"
        system(f"wget -q -O {file} -c {url} \n"
               f"sudo dpkg -i {file} \n"
               f"echo [Installed] - {program}")

    return None


def update_upgrade() -> None:
    system(f"sudo apt update && sudo apt dist-upgrade -y \n"
           f"flatpak update \n"
           f"sudo apt autoclean \n"
           f"sudo apt autoremove -y")
    return None


def apt_update() -> None:
    system("sudo apt update -y")
    return None


def install_brave() -> None:
    system("sudo apt install apt-transport-https curl -y \n"
           "sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg "
           "https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg -y \n"
           "echo deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] "
           "https://brave-browser-apt-release.s3.brave.com/ stable main "
           "| sudo tee /etc/apt/sources.list.d/brave-browser-release.list")
    return None


def install_anydesk() -> None:
    system("wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | apt-key add - \n"
           "echo deb http://deb.anydesk.com/ all main > /etc/apt/sources.list.d/anydesk-stable.list")
    return None


def final_message() -> None:
    print("All installations have been completed!")
    return None


def create_symlinks(symlinks: Dict[str, Symlink]) -> None:
    for _, symlink in symlinks.items():
        system(f"rm {symlink.destiny()} \n"
               f"ln -s {symlink.origin()} {symlink.destiny()}")
        print(f"[Linked] - {symlink.name()}")

    return None


def install_orico_adapter() -> None:
    # https://plus.diolinux.com.br/t/review-adaptador-bluetooth-orico-bta-508-no-linux/35393
    # https://www.xmpow.com/pages/download
    # buscar por "BH456A"
    driver_link: str = "https://mpow.s3-us-west-1.amazonaws.com/20201202_mpow_BH456A_driver+for+Linux.7z"
    system(f"wget -c {driver_link} -P {DOWNLOADS} \n"
           f"7z x 20201202_mpow_BH456A_driver+for+Linux.7z \n"
           f"sudo cp -iv {DOWNLOADS}/20201202_LINUX_BT_DRIVER/rtkbt-firmware/lib/firmware/rtlbt/rtl8761b_fw "
           f"/lib/firmware/rtl_bt/rtl8761b_fw.bin \n"
           f"sudo cp -iv {DOWNLOADS}/20201202_LINUX_BT_DRIVER/rtkbt-firmware/lib/firmware/rtlbt/rtl8761b_config "
           f"/lib/firmware/rtl_bt/rtl8761b_config.bin"
           )
    return None


def change_icon_dir(icons: Dict[str, str]) -> None:
    for target, icon in icons.items():
        system(f"gio set -t string '{target}' metadata::custom-icon 'file://{icon}'")
    return None
