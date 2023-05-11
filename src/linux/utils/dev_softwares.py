from src.utils.arrows import create_title
from questionary import checkbox
import subprocess

curl_install_command = ["sudo", "apt", "install", "curl", "-y"]
wget_install_command = ["sudo", "apt", "install", "wget", "-y"]
npm_install_command = ["sudo", "apt", "install", "npm", "-y"]

all_commands = [
    curl_install_command,
    wget_install_command,
    npm_install_command,
]


def install_nvm():

    subprocess.run([
        "curl",
        "-o",
        "install.sh",
        "https://raw.githubusercontent.com/creationix/nvm/master/install.sh"
    ])
    subprocess.run(["bash", "install.sh"])


def install_dev_softwares():
    options = [
        {"name": "all", "checked": False},
        {"name": "curl", "checked": False},
        {"name": "wget", "checked": False},
        {"name": "npm", "checked": False},
        {"name": "nvm",  "checked": False},
    ]

    selected_options = checkbox(
        "Select the softwares you want to install",
        choices=options
    ).ask()

    if "all" in selected_options:
        create_title("Installing all softwares")

        for command in all_commands:
            create_title("Installing " + command[2])
            subprocess.run(command)
        install_nvm()
    else:
        if "curl" in selected_options:
            create_title("Installing curl")
            subprocess.run(curl_install_command)
        if "wget" in selected_options:
            create_title("Installing wget")
            subprocess.run(wget_install_command)
        if "npm" in selected_options:
            create_title("Installing npm")
            subprocess.run(npm_install_command)
        if "nvm" in selected_options:
            create_title("Installing nvm")
            install_nvm()

    create_title("All development softwares installed")
