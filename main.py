from sys import argv

from src.desktop_apps import update_all_packages
from src.functions import *
from src.general_apps import *

if __name__ == "__main__":
    # exit(0)
    try:
        is_desktop: bool = bool(argv[1])
    except IndexError:
        is_desktop = False

    if is_desktop:
        update_all_packages(ppas=ppas, deb=deb_to_url,
                            apt_packages=apt_packages,
                            remove_apt_packages=remove_apt_packages,
                            flatpak_packages=flatpak_packages,
                            symlinks=symlinks, icons=icons, mkdir=mkdir)

    # install_brave()
    # install_anydesk()
    make_directories(mkdir=mkdir)
    apt_update()
    add_apt_repository(programs=ppas)
    apt_update()
    install_apt(programs=apt_packages)
    apt_update()
    install_deb(programs=deb_to_url)
    apt_update()
    install_flatpaks(programs=flatpak_packages)
    remove_apt(programs=remove_apt_packages)
    update_upgrade()
    pip()
    create_symlinks(symlinks=symlinks)
    copy_file(copy_files=copy_files)
    final_message()
