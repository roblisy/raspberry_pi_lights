# Raspberry_Lights

A simple Python script for controlling my exterior house lights using a Raspberry Pi and a relay. 
I'm using the [8 unit relay found here](https://www.sainsmart.com/products/8-channel-5v-relay-module), with wiring 
as [described on this YouTube video](https://www.youtube.com/watch?v=oaf_zQcrg7g).  

Setup:  
    
    sudo apt update  
    sudo apt install python3  
    mkdir ~/raspberry_lights
    cd ~/raspberry_lights
    git clone git@github.com:roblisy/raspberry_pi_lights.git
    pip install -r requirements.txt

The script (lights.py) has some small requirements at top and uses Python 3. It should be setup to run as a service 
using [system.md](https://www.raspberrypi.org/documentation/linux/usage/systemd.md). Make sure you:

    sudo cp lights.service /etc/systemd/system/lights.service    
    sudo systemctl enable lights.service  
    
    
### Configuration

Most things should be controllable using variables.
    
    sleep_seconds = number of seconds to sleep code execution in the loop
    mins_before_sunset = number of minutes prior to sunset to turn the lights on
    off_at_hour_minute = local time to turn the lights off
    tz = local time zone