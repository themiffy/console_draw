import console_draw
import pytest


def test_set_first_pixel():
    test_disp = console_draw.Display(console_draw.SCREEN_SIZE_X, console_draw.SCREEN_SIZE_Y)
    test_disp.set_pixel(0, 0)
    test_disp._make_frame_string() # only for test 
    assert test_disp.frame_string[0] == '#'

def test_set_first_pixel_another_symbol():
    test_disp = console_draw.Display(console_draw.SCREEN_SIZE_X, console_draw.SCREEN_SIZE_Y, symbol = '*')
    test_disp.set_pixel(0, 0)
    test_disp._make_frame_string() # only for test 
    assert test_disp.frame_string[0] == '*'

def test_set_first_pixel_incorrect_symbol():
    test_disp = console_draw.Display(console_draw.SCREEN_SIZE_X, console_draw.SCREEN_SIZE_Y, symbol = 'string length must be 1')
    test_disp.set_pixel(0, 0)
    test_disp._make_frame_string() # only for test 
    assert test_disp.frame_string[0] == 's'

def test_set_first_pixel_special_sym():
    test_disp = console_draw.Display(console_draw.SCREEN_SIZE_X, console_draw.SCREEN_SIZE_Y, symbol = '\n')
    test_disp.set_pixel(0, 0)
    test_disp._make_frame_string() # only for test 
    assert test_disp.frame_string[0] == '#'

def test_set_last_pixel():
    ''' Max pixel coord is 1 less thas size (pixel count starts with 0) '''

    test_disp = console_draw.Display(console_draw.SCREEN_SIZE_X, console_draw.SCREEN_SIZE_Y)
    test_disp.set_pixel(console_draw.SCREEN_SIZE_X - 1, console_draw.SCREEN_SIZE_Y - 1)
    test_disp._make_frame_string() # only for test 
    assert test_disp.frame_string[-1] == '#'