#!/usr/bin/env python3

import time
from aiy.leds import (Leds, Pattern, Color)

with Leds() as leds:
    print('Set breathe pattern: period=1000ms (1Hz)')
    print('RGB: Breathe RED for 5 seconds')
    leds.pattern = Pattern.breathe(1000)
    leds.update(Leds.rgb_pattern(Color.PURPLE))
    while True:
        time.sleep(5)

