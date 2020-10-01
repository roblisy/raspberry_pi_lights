# Goal:
# A script to turn on and off relays connected to the Rasbperry Pi GPIO pins at certain times of the day.
# These relays can be connected to an outdoor lighting setup

# Imports...
import astral
import datetime
import pytz
from astral.sun import sun
import logging
import RPi.GPIO as GPIO
import time

# Set your location here
tz = "America/Los_Angeles"
location = astral.LocationInfo(
    name="Seattle",
    region="USA",
    timezone=tz,
    latitude=47.6304,
    longitude=-122.3631)

# how long to sleep our loop for...
sleep_seconds = 3

# GPIO pins for Raspberry Pi
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pinList = [2, 3, 4, 17, 27, 22, 10, 9]

logging.basicConfig(filename='lights.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def get_sunset_sunrise(loc, dt):
    """
    Function to get the sunrise and sunset at a location
    :param loc: location to deterimine the sunrise / sunset
    :param dt: date to determin the sunrise / sunset for
    :return:
    """
    l = sun(loc.observer, date=dt, tzinfo=loc.timezone)
    logging.debug("""Sunrise at l["sunrise"]""")
    return l["sunrise"], l["sunset"]


def ctrl_lights(state):
    """
    Function to turn on and off all of the relays
    :return:
    """
    if state == 'off':
        for i in pinList:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.HIGH)

    if state == 'on':
        for i in pinList:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.LOW)


def get_user_input():
    """
    Silly testing function to switch control of the relays over to the user instead of a timer.
    :return: state
    """
    state = input("Enter light state (on/off): ")
    print(f"Turning lights {state}")
    ctrl_lights(state=state)


def main():
    # Make a loop that runs forever. It should
    # - check the current time
    # - compare the current time to sunset
    # - if the current time is within 30 minutes of sunset, turn on the lights
    # - if the current time is after 11 pm, turn off the lights.

    while True:
        now = pytz.timezone(tz).localize(datetime.datetime.now())
        today = datetime.date.today()

        # turn off the lights at 11:30 pm, local time
        turn_off_at = pytz.timezone(tz).localize(datetime.datetime.combine(today, datetime.time(23, 30)))
        # print(f"Now: {now}")
        # print(f"Off: {turn_off_at}")
        sunrise, sunset = get_sunset_sunrise(loc=location, dt=today)

        # uncomment below to use user input instead of date time...
        # get_user_input()
        print('Currently running python3 /home/pi/raspberry_lights/lights.py from /etc/rc.local...')
        # if now is 30 minutes before sunset, turn the lights on...
        if (now >= sunset) & (now <= turn_off_at):
            ctrl_lights("on")

        if now >= turn_off_at:
            ctrl_lights("off")
        time.sleep(sleep_seconds)


# Call the main function
if __name__ == "__main__":
    main()
