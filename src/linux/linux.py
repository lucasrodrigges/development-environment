from src.utils.arrows import left_arrow, right_arrow
import subprocess
from src.linux.utils.dev_softwares import install_dev_softwares

def system_update():
    print(right_arrow + "Updating system" + left_arrow)
    subprocess.run(["sudo", "apt", "update", "-y"])
    subprocess.run(["sudo", "apt", "upgrade", "-y"])

def customize_terminal():
    print(right_arrow + "Customizing terminal" + left_arrow)
    subprocess.run(["sudo", "apt", "install", "zsh", "-y"])
    subprocess.run(["sh", "-c", "'$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)'"])
    subprocess.run(["sudo", "chsh," "-s", "$(which zsh)"])

def linux_script():
    system_update()
    customize_terminal()
    install_dev_softwares()
