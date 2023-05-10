import os
import subprocess
from src.linux.utils.dev_softwares import install_dev_softwares

from src.utils.arrows import left_arrow, right_arrow

current_dir = os.getcwd()


def system_update():
    print(right_arrow + "Updating system" + left_arrow)

    subprocess.run(["sudo", "apt", "update", "-y"])
    subprocess.run(["sudo", "apt", "upgrade", "-y"])


def linux_script():
    system_update()
    install_dev_softwares()
