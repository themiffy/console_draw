import os
import sys
import time
from art import text2art
import numpy as np
from typing import Tuple, Union

SCREEN_SIZE_X = 80
SCREEN_SIZE_Y = 24


def draw() -> None:
    for i in range(80):
        time.sleep(0.075)
        sys.stdout.write("\r" + '.'*i)
        sys.stdout.flush()

        
    print('\n\n'+ text2art('GAVNO'))


class Display:
    def __init__(self, x_size: int, y_size: int) -> None:
        '''Initialize fields and generate pixels list'''

        self.x_size: int = x_size
        self.y_size: int = y_size
        self.__pixels = [[' ' for _ in range(self.x_size)] for _ in range(self.y_size)]

    def draw(self) -> None:
        '''Generate string out of the pixels list and draw it single time'''

        self._make_frame_string()
        print(self.frame_string)

    def set_pixel(self, x: int, y: int) -> None:
        ''' Debug function setting pixel '''
        #print(len(self.__pixels), len(self.__pixels[1]))
        self.__pixels[y][x] = '#'

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



if __name__ == '__main__':
    display = Display(SCREEN_SIZE_X, SCREEN_SIZE_Y)
    display.draw()

    while True:
        input_value = pixel_input('Draw x y: ')
        if input_value: 
            x, y = input_value
            display.set_pixel(x, y)
            display.draw()