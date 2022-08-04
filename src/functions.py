from os import system
from typing import List, Dict


# TODO: bookmarks, mount disks (/etc/fstab), change directories icons, mkdir
PYTHON_VERSION: str = f"python3.9"
HOME: str = "$HOME"
APPS_DIRECTORY: str = f"{HOME}/Downloads/Applications"
APPIMAGE_DIRECTORY: str = f"{APPS_DIRECTORY}/deb"
DEB_DIRECTORY: str = f"{APPS_DIRECTORY}/AppImage"


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
