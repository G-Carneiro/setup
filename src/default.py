from typing import List, Dict

from .Symlink import Symlink
from .global_variables import *

# Manually install
# bitwarden   https://bitwarden.com/download/
# toolbox     https://www.jetbrains.com/toolbox-app/
# pandoc      https://github.com/jgm/pandoc/releases/latest
# pcloud      https://www.pcloud.com/download-free-online-cloud-file-storage.html

# This install all applications I need in post install linux distribution based in debian.
# FIXME: wait brave-browser, anydesk, bitwarden, toolbox, pandoc and pcloud
#  release auto update apt or oficial flatpak support or generic link download (agnostic version).
# TODO: install pympress by default or not? https://github.com/Cimbali/pympress/
# TODO: OnionShare or RetroShare?
# TODO: fdm or chrono?
# TODO: .config/mimeapps.list
# TODO: dconf dump /prg/cinnamon [>|<] file.txt

ppas: List[str] = []

deb_to_url: Dict[str, str] = {
    "discord": "https://discord.com/api/download?platform=linux&format=deb",
    "mailspring": "https://updates.getmailspring.com/download?platform=linuxDeb",
    # "google_chrome": "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb",
    "freedownloadmanager": "https://dn3.freedownloadmanager.org/6/latest/freedownloadmanager.deb"
}

apt_packages: List[str] = [
    # "anydesk",
    # "brave-browser",
    "git",
    "gnome-clocks",
    "grub-customizer",
    "inkscape",                 # flatpak version not support some features for tex files
    "pdf2svg",
    f"{PYTHON_VERSION}-dev",
    f"{PYTHON_VERSION}-dbg",
    f"{PYTHON_VERSION}-full",
    "python3-pip",
    "python3-pygments",
    "python3-tk-dbg",
    "shellcheck",
    "spotify-client",
    "texlive-full"
]

flatpak_packages: Dict[str, str] = {
    "barrier": "com.github.debauchee.barrier",          # official support
    "blackbox": "com.raggesilver.BlackBox",             # official support
    "colorway": "io.github.lainsce.Colorway",           # official support
    "emulsion": "io.github.lainsce.Emulsion",           # official support
    "flameshot": "org.flameshot.Flameshot",             # official support
    "flatseal": "com.github.tchx84.Flatseal",           # official support
    # "neovim": "io.neovim.nvim",                         # official support
    "telegram": "org.telegram.desktop",                 # official support
    "xournalpp": "com.github.xournalpp.xournalpp",      # official support
    "whatsapp": "io.github.mimbrero.WhatsAppDesktop",   # unofficial support
}

remove_apt_packages: List[str] = [
    "firefox",
    "firefox-locale-en",
    "firefox-locale-pt",
    "hexchat-common",
    f"idle-{PYTHON_VERSION}",
    "libreoffice-common",
    "sticky",                   # notes
    "thunderbird"               # email manager
]

symlinks: Dict[str, Symlink] = {
    "gitconfig": Symlink(name="gitconfig", origin=f"{DEFAULT_CONFIG}", destiny=f"{HOME}", file=".gitconfig"),
    "Mailspring-key": Symlink(name="Mailspring", origin=f"{DEFAULT_CONFIG}", destiny=f"{CONFIG}", file="keymap.json"),
    "Mailspring-pref": Symlink(name="Mailspring", origin=f"{DEFAULT_CONFIG}", destiny=f"{CONFIG}", file="Preferences"),
    "telegram": Symlink(name="telegram", origin=f"{DEFAULT_CONFIG}", destiny=f"{VAR_APP}",
                        file="shortcuts-custom.json"),
    "whatsapp-pref": Symlink(name="whatsapp", origin=f"{DEFAULT_CONFIG}", destiny=f"{VAR_APP}", file="Preferences")
}

copy_files: Dict[str, Symlink] = {
    "discord": Symlink(name="discord", origin=f"{DEFAULT_CONFIG}", destiny=f"{CONFIG}", file="settings.json"),
    "whatsapp-conf": Symlink(name="whatsapp", origin=f"{DEFAULT_CONFIG}", destiny=f"{VAR_APP}", file="config.json")
}

icons: Dict[str, str] = {
    f"{GIT}": f"{ICONS}/folder-github.svg"
}

mkdir: List[str] = [
    GIT,
    APPS_DIRECTORY,
    APPIMAGE_DIRECTORY,
    DEB_DIRECTORY
]

dconf: Dict[str, str] = {
    "/org/cinnamon/desktop/keybindings/": f"{DEFAULT_CONFIG}/dconf/keybindings.txt"
}
