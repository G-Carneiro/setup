from os import scandir
from os import system
from typing import List, Dict

from .Symlink import Symlink
from .global_variables import *


def add_apt_repository(programs: List[str]) -> None:
    for program in programs:
        system(f"sudo add-apt-repository ppa:{program} -y \n"
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
           f"sudo apt --fix-broken install -y \n"
           f"flatpak update -y \n"
           f"sudo apt autoclean \n"
           f"sudo apt autoremove -y")
    return None


def apt_update() -> None:
    system("sudo apt update -y")
    return None


def install_brave() -> None:
    link: str = "https://brave-browser-apt-release.s3.brave.com/"
    keyring_link: str = "https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg"
    signed: str = "[signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64]"
    system(f"sudo apt install apt-transport-https curl -y \n"
           f"sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg {keyring_link} \n"
           f"echo 'deb {signed} {link} stable main'|sudo tee /etc/apt/sources.list.d/brave-browser-release.list")
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


def change_icon_dir(icons_dir: str = f"{ICONS}",
                    target_dir: str = f"{HOME}") -> None:
    for icon in scandir(icons_dir):
        icon_name: str = icon.name
        for target_file in scandir(target_dir):
            target_name: str = target_file.name
            if target_file.is_dir() \
                    and (icon_name.lower().replace(" ", "-")[:-4] in target_name.lower().replace(" ", "-")):
                if icon.is_file():
                    target_path = target_file.path
                    icon_path = icon.path
                    system(f"gio set -t string '{target_path}' metadata::custom-icon "
                           f"'file://{icon_path}'")
                else:
                    change_icon_dir(icons_dir=icon.path, target_dir=target_file.path)
                break
    return None


def copy_file(copy_files: Dict[str, Symlink]) -> None:
    for _, value in copy_files.items():
        system(f"cp {value.origin()} {value.destiny()} \n"
               f"chmod 400 {value.destiny()}")
        print(f"[Copied] - {value.name()}")
    return None


def pip() -> None:
    system("pip install --upgrade pip")
    return None


def make_directories(mkdir: List[str]) -> None:
    for dir_ in mkdir:
        system(f"mkdir {dir_}")
        print(f"[Created] - {dir_}")
    return None


def apply_dconf(dconf: Dict[str, str]) -> None:
    for key, value in dconf.items():
        system(f"dconf load {key} < {value}")
        print(f"[Config] - {key}")
    return None
