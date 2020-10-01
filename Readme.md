# Raspberry_Lights

A simple Python script for controlling my exterior house lights using a Raspberry Pi and a relay.

Setup:  
    
    sudo apt update  
    sudo apt full-upgrade  
    sudo reboot
    sudo apt install python3  
    
    pip install -r requirements.txt

The script (lights.py) has some small requirements at top and uses Python 3. It should be setup to run as a service 
using [system.md](https://www.raspberrypi.org/documentation/linux/usage/systemd.md). Make sure you:

    sudo cp lights.service /etc/systemd/system/lights.service    
    sudo systemctl enable lights.service  