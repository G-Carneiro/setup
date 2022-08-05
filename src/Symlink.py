from typing import Dict

from .global_variables import *

flatpak_to_folder: Dict[str, str] = {
    "telegram": f"org.telegram.desktop/data/TelegramDesktop/tdata",
    "whatsapp": f"io.github.mimbrero.WhatsAppDesktop/config/whatsapp-desktop-linux"
}


class Symlink:
    def __init__(self, name: str, origin: str, destiny: str, file: str):
        self._name: str = name
        self._file: str = file
        self._origin: str = f"{origin}/{name}/{file}"
        self._destiny: str = f"{destiny}/"
        if (destiny == VAR_APP):
            self._destiny += f"{flatpak_to_folder[name]}/{file}"
        elif (destiny == HOME):
            self._destiny += f"{file}"
        else:
            self._destiny += f"{name}/{file}"

    def name(self) -> str:
        return self._name

    def origin(self) -> str:
        return self._origin

    def destiny(self) -> str:
        return self._destiny
