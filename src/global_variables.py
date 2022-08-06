from os.path import dirname, abspath


PYTHON_VERSION: str = f"python3.9"
HOME: str = "$HOME"
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
