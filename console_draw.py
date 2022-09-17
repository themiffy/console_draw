#import os
import sys
#from art import text2art
#import numpy as np
import time

from typing import Tuple, Union

SCREEN_SIZE_X = 80
SCREEN_SIZE_Y = 24

class Display:

    def __init__(self, x_size: int, y_size: int, symbol: str = '#', empty_space_symbol: str = ' ') -> None:
        '''Initialize fields and generate pixels list'''

        if ord(symbol[0]) < 32: 
            self.symbol = '#'
        else: 
            self.symbol: str = symbol[0] # Makes sure length is 1

        self.x_size: int = x_size
        self.y_size: int = y_size
        self.empty_space_symbol = empty_space_symbol
        self.__pixels = [[self.empty_space_symbol for _ in range(self.x_size)] for _ in range(self.y_size)]

    def draw(self) -> None:
        '''Generate string out of the pixels list and draw it single time'''

        self._make_frame_string()

        sys.stdout.write(u"\u001b[1000D") # does not work
        sys.stdout.flush()

        sys.stdout.write(self.frame_string)

        


    def set_pixel(self, x: int, y: int) -> None:
        ''' Debug function setting pixel '''

        self.__pixels[y][x] = self.symbol
            
    def clear(self) -> None:
        ''' Reinitialize with same parameters'''

        self.__init__(self.x_size, self.y_size, symbol = self.symbol, empty_space_symbol = self.empty_space_symbol)

    def _make_frame_string(self) -> None:
        ''' Generate string out of pixels list '''

        self.frame_string: str = ''.join([''.join(row)+'\n' for row in self.__pixels])[:-1]

def pixel_input(message) -> Union[Tuple, None]:
    command: str = input(message)
    command = command.replace(',', ' ')
    try:
        pixel_position = tuple([int(value.strip()) for value in command.strip().split()])
        return pixel_position
    except ValueError:
        print('Incorrect x y')
        return None
    except Exception as e:
        print(e)
        return None


FRAME_COUNT = 0
V1 = [(40, 12), (41, 12), (41, 13), (40, 13)]
def circle(radius):
    global FRAME_COUNT
    global V1

    FRAME_COUNT += 1 if FRAME_COUNT != 3 else -3
    return V1[FRAME_COUNT]

if __name__ == '__main__':
    display = Display(SCREEN_SIZE_X, SCREEN_SIZE_Y)
    display.draw()

    x = 0

    while True:
        x, y = circle(1)
        display.clear()
        display.set_pixel(x, y)
        display.draw()
        time.sleep(0.1)


    # while True:
    #     input_value = pixel_input('Draw x y: ')
    #     if input_value: 
    #         x, y = input_value
    #         display.set_pixel(x, y)
    #         display.draw()