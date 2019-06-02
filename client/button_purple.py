#!/usr/bin/env python3

from aiy.board import Board, Leds, Color

print('LED is ON while button is pressed (Ctrl-C for exit).')
with Board() as board:
    with Leds() as leds:
        while True:
            board.button.wait_for_press()
            print('ON')
            leds.update(Leds.rgb_on(Color.PURPLE))
            board.button.wait_for_release()
            print('OFF')
            leds.update(Leds.rgb_off())

