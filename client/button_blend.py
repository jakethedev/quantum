#!/usr/bin/env python3

import time
from aiy.leds import (Leds, Color)

with Leds() as leds:
    print('RGB: Blend between PURPLE and BLUE over 3 seconds')
    for i in range(30):
        color = Color.blend(Color.BLUE, Color.PURPLE, i / 30)
        leds.update(Leds.rgb_on(color))
        time.sleep(0.1)

    print('RGB: Blend between GREEN and BLUE over 3 seconds')
    for i in range(30):
        color = Color.blend(Color.BLUE, Color.GREEN, i / 30)
        leds.update(Leds.rgb_on(color))
        time.sleep(0.1)
