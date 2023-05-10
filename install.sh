#!/bin/bash

echo "Installing Python 3..."
sudo apt-get install python3 python3-pip python3.10-venv -y 

python3 -m venv .venv && . .venv/bin/activate && python3 -m pip install -r requirements.txt

python3 main.py