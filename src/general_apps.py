from typing import List, Dict

from .functions import PYTHON_VERSION


# Manually install
# bitwarden   https://bitwarden.com/download/
# toolbox     https://www.jetbrains.com/toolbox-app/
# pandoc      https://github.com/jgm/pandoc/releases/latest
# pcloud      https://www.pcloud.com/download-free-online-cloud-file-storage.html

# This install all applications I need in post install linux distribution based in debian.
# FIXME: wait brave-browser, anydesk, bitwarden, toolbox, pandoc and pcloud
#  release auto update apt or oficial flatpak support or generic link download (agnostic version).
# TODO: install pympress by default or not? https://github.com/Cimbali/pympress/

ppas: List[str] = []

deb_to_url: Dict[str, str] = {
    "discord": "https://discord.com/api/download?platform=linux&format=deb",
    "mailspring": "https://updates.getmailspring.com/download?platform=linuxDeb",
    "google_chrome": "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb",
    "freedownloadmanager": "https://dn3.freedownloadmanager.org/6/latest/freedownloadmanager.deb"
}

apt_packages: List[str] = [
    "anydesk",
    "brave-browser",
    "git",
    "gnome-clocks",
    "grub-customizer",
    "pdf2svg",
    f"{PYTHON_VERSION}-dev",
    f"{PYTHON_VERSION}-dbg",
    f"{PYTHON_VERSION}-full",
    "python3-pip",
    "python3-tk-dbg",
    "shellcheck",
    "spotify-client",
    "texlive-full",
    "whatsapp-desktop"        # wait official support
]

flatpak_packages: Dict[str, str] = {
    "barrier": "com.github.debauchee.barrier",      # official support
    "colorway": "io.github.lainsce.Colorway",       # official support
    "emulsion": "io.github.lainsce.Emulsion",       # official support
    "flameshot": "org.flameshot.Flameshot",         # official support
    "inkscape": "org.inkscape.Inkscape",            # official support
    "neovim": "io.neovim.nvim",                     # official support
    "telegram": "org.telegram.desktop",             # official support
    "xournalpp": "com.github.xournalpp.xournalpp"   # official support
}

remove_apt: List[str] = [
    "firefox",
    "firefox-locale-en",
    "firefox-locale-pt",
    "hexchat-common",
    f"idle-{PYTHON_VERSION}",
    "libreoffice-common",
    "sticky",                   # notes
    "thunderbird"               # email manager
]
