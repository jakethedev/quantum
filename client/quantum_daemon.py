#!/usr/bin/env python3
import requests, sys, time
from aiy.board import Board, Color, Leds, Pattern

# Judge not, ye who enter here, for this was fun and awesome.
try: 
    if (len(sys.argv) == 1):
        print("ERR: Must pass base server url as first argument!")
        exit(1)
    BASE_URL = sys.argv[1]
    TOGGLE_URL = "%s/toggle" % BASE_URL
    STATUS_URL = "%s/status" % BASE_URL

    with Board() as board, Leds() as led:
        board.button.when_pressed = lambda: requests.get(TOGGLE_URL)
        while True:
            status = requests.get(STATUS_URL)
            if (status.status_code == 200):
                if (status.text == 'false'):
                    led.update(Leds.rgb_off())
                elif (status.text == 'true'):
                    led.update(Leds.rgb_on(Color.PURPLE))
            time.sleep(0.15)

except Exception as e:
    print("Error toggling state, check server!")

