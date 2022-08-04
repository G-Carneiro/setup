from sys import argv

from src.desktop_apps import *
from src.functions import *
from src.general_apps import *

if __name__ == "__main__":
    try:
        is_desktop: bool = bool(argv[1])
    except IndexError:
        is_desktop = False

    if is_desktop:
        ppas += desktop_ppas
        apt_packages += desktop_apt_packages
        remove_apt_packages += desktop_remove_apt_packages
        deb_to_url.update(desktop_deb_to_url)
        flatpak_packages.update(desktop_flatpak_packages)

    install_brave()
    install_anydesk()
    apt_update()
    add_apt_repository(programs=ppas)
    apt_update()
    install_apt(programs=apt_packages)
    install_deb(programs=deb_to_url)
    apt_update()
    install_flatpaks(programs=flatpak_packages)
    remove_apt(programs=remove_apt_packages)
    update_upgrade()
    final_message()
