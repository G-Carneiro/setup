from os import system
from typing import List, Dict


PYTHON_VERSION: str = f"python3.9"
APPS_DIRECTORY: str = "/home/gabriel/Downloads/Applications"
APPIMAGE_DIRECTORY: str = f"{APPS_DIRECTORY}/deb"
DEB_DIRECTORY: str = f"{APPS_DIRECTORY}/AppImage"


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


