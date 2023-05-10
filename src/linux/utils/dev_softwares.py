from src.utils.arrows import left_arrow, right_arrow
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
    subprocess.run(nvm_install_command=[[
        "curl",
        "-o",
        "install.sh",
        "https://raw.githubusercontent.com/creationix/nvm/master/install.sh"
    ]])
    subprocess.run(["bash", "install.sh"])
    profile = "~/.bashrc"
    subprocess.run(["source", profile])


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
        print(right_arrow + "Installing all softwares" + left_arrow)

        for command in all_commands:
            print(right_arrow + "Installing " + command[3] + left_arrow)
            subprocess.run(command)
        install_nvm()
    else:
        if "curl" in selected_options:
            print(right_arrow + "Installing curl" + left_arrow)
            subprocess.run(curl_install_command)
        if "wget" in selected_options:
            print(right_arrow + "Installing wget" + left_arrow)
            subprocess.run(wget_install_command)
        if "npm" in selected_options:
            print(right_arrow + "Installing npm" + left_arrow)
            subprocess.run(npm_install_command)
        if "nvm" in selected_options:
            print(right_arrow + "Installing nvm" + left_arrow)
            install_nvm()

    print(right_arrow + "All de softwares installed" + left_arrow)
