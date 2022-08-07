from os.path import dirname, abspath, expanduser


PYTHON_VERSION: str = f"python3.9"
HOME: str = expanduser("~")
GIT: str = f"{HOME}/Git"
VAR: str = f"{HOME}/.var"
VAR_APP: str = f"{VAR}/app"
THIS: str = f"{dirname(abspath('__main__'))}"
DOTFILES: str = f"{THIS}/dotfiles"
NOTE_CONFIG: str = f"{DOTFILES}/note"
DESKTOP_CONFIG: str = f"{DOTFILES}/desktop"
CONFIG: str = f"{HOME}/.config"
DOWNLOADS: str = f"{HOME}/Downloads"
APPS_DIRECTORY: str = f"{DOWNLOADS}/Applications"
APPIMAGE_DIRECTORY: str = f"{APPS_DIRECTORY}/deb"
DEB_DIRECTORY: str = f"{APPS_DIRECTORY}/AppImage"
PCLOUD: str = f"{HOME}/pCloudDrive"
IMG: str = f"{THIS}/img"
ANIMES: str = f"{HOME}/Animes"
ICONS: str = f"{PCLOUD}/Icons"
CCO: str = f"{HOME}/CCO"
