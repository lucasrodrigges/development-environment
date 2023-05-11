import platform
from src.linux.linux import linux_script
from src.utils.arrows import create_title

create_title("Welcome to the setup script")

system = platform.system()

if system == "Linux":
    linux_script()
