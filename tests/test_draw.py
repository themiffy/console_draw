import console_draw
import pytest


def test_set_first_pixel():
    test_disp = console_draw.Display(console_draw.SCREEN_SIZE_X, console_draw.SCREEN_SIZE_Y)
    test_disp.set_pixel(0, 0)
    test_disp._make_frame_string() # only for test 
    assert test_disp.frame_string[0] == '#'

def test_set_last_pixel():
    ''' Max pixel coord is 1 less thas size (pixel count starts with 0) '''

    test_disp = console_draw.Display(console_draw.SCREEN_SIZE_X, console_draw.SCREEN_SIZE_Y)
    test_disp.set_pixel(console_draw.SCREEN_SIZE_X - 1, console_draw.SCREEN_SIZE_Y - 1)
    test_disp._make_frame_string() # only for test 
    assert test_disp.frame_string[-1] == '#'