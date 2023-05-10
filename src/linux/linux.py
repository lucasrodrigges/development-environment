import os
import subprocess
from src.utils.arrows import left_arrow, right_arrow
from src.linux.utils.dev_softwares import install_dev_softwares

current_dir = os.getcwd()


def system_update():
    print(right_arrow + "Updating system" + left_arrow)

    subprocess.run(["sudo", "apt", "update", "-y"])
    subprocess.run(["sudo", "apt", "upgrade", "-y"])


def customize_terminal():
    print(right_arrow + "Customizing terminal" + left_arrow)

    subprocess.run(["sudo", "apt", "install", "zsh", "-y"])
    subprocess.run([
        "wget",
        "https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh",
        "&&",
        "sh",
        "install.sh"
    ])
    subprocess.run(["sudo", "chsh", "-s", "$(which zsh)"])
    subprocess.run([
        "git",
        "clone",
        "https://github.com/zsh-users/zsh-syntax-highlighting.git",
        "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting"
    ])
    subprocess.run([
        "git",
        "clone",
        "https://github.com/zsh-users/zsh-autosuggestions",
        "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions"
    ])

    with open("~/.zshrc", "a") as file:
        file.write('export ZSH="$HOME/.oh-my-zsh"\n')
        file.write('ZSH_THEME="robbyrussell"\n')
        file.write(
            'plugins=(git zsh-syntax-highlighting zsh-autosuggestions)\n'
        )


def linux_script():
    system_update()
    customize_terminal()
    install_dev_softwares()
