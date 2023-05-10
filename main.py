# import subprocess
import platform
from src.linux.linux import linux_script

print("Welcome to the Development Environment Setup Script")

system = platform.system()

if system == "Linux":
    linux_script()
