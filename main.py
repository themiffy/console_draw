import os
import sys
import time
from art import text2art
import numpy as np

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

        self.frame_string: str = ''.join([''.join(row)+'\n' for row in self.__pixels])


if __name__ == '__main__':
    display = Display(80, 24)
    #display.set_pixel(12, 12)
    #display.set_pixel(12, 13)
    #display.set_pixel(13, 12)
    #display.set_pixel(13, 13)
    display.draw()
    while True:
        command: str = input('draw x y: ')
        pixel_position = [int(i) for i in command.split()]
        display.set_pixel(pixel_position[0], pixel_position[1])
        display.draw()