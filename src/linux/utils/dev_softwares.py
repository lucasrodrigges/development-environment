from src.utils.arrows import left_arrow, right_arrow
from questionary import checkbox
import subprocess

curl_install_command = ["sudo", "apt", "install", "curl", "-y"]
wget_install_command = ["sudo", "apt", "install", "wget", "-y"]
git_install_command = ["sudo", "apt", "install", "git", "-y"]
npm_install_command = ["sudo", "apt", "install", "npm", "-y"]

all_commands = [
    curl_install_command,
    wget_install_command,
    git_install_command,
    npm_install_command
]

def install_dev_softwares():
    options = [
        {"name": "all", "checked": False},
        {"name": "curl", "checked": False},
        {"name": "wget", "checked": False},
        {"name": "git", "checked": False},
        {"name": "npm", "checked": False},
    ]

    selected_options = checkbox(
        "Select the softwares you want to install",
        choices=options
    ).ask()

    if "all" in selected_options:
        print(right_arrow + "Installing all softwares" + left_arrow)
        
        for command in all_commands:
            subprocess.run(command)
    else:
        if "curl" in selected_options:
            print(right_arrow + "Installing curl" + left_arrow)
            subprocess.run(curl_install_command)
        if "wget" in selected_options:
            print(right_arrow + "Installing wget" + left_arrow)
            subprocess.run(wget_install_command)
        if "git" in selected_options:
            print(right_arrow + "Installing git" + left_arrow)
            subprocess.run(git_install_command)
        if "npm" in selected_options:
            print(right_arrow + "Installing npm" + left_arrow)
            subprocess.run(npm_install_command)