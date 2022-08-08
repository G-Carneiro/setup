from os.path import dirname, abspath, expanduser


PYTHON_VERSION: str = f"python3.10"
HOME: str = expanduser("~")
GIT: str = f"{HOME}/Git"
VAR: str = f"{HOME}/.var"
MNT: str = f"/mnt"
VAR_APP: str = f"{VAR}/app"
THIS: str = f"{dirname(abspath('__main__'))}"
DOTFILES: str = f"{THIS}/dotfiles"
DEFAULT_CONFIG: str = f"{DOTFILES}/default"
DESKTOP_CONFIG: str = f"{DOTFILES}/desktop"
CONFIG: str = f"{HOME}/.config"
DOWNLOADS: str = f"{HOME}/Downloads"
APPS_DIRECTORY: str = f"{DOWNLOADS}/Applications"
APPIMAGE_DIRECTORY: str = f"{APPS_DIRECTORY}/AppImage"
DEB_DIRECTORY: str = f"{APPS_DIRECTORY}/deb"
PCLOUD: str = f"{HOME}/pCloudDrive"
ICONS: str = f"{PCLOUD}/Icons"
