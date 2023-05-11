import subprocess
from src.linux.utils.dev_softwares import install_dev_softwares

from src.utils.arrows import create_title


def system_update():
    create_title("Updating system")

    subprocess.run(["sudo", "apt", "update", "-y"])
    subprocess.run(["sudo", "apt", "upgrade", "-y"])


def linux_script():
    system_update()
    install_dev_softwares()
