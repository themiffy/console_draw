import gavno
import pytest


def test_set_first_pixel():
    test_disp = gavno.Display(80, 24)
    test_disp.set_pixel(0, 0)
    test_disp._make_frame_string() # only for test 
    assert test_disp.frame_string[0] == '#'

def test_set_last_pixel():
    test_disp = gavno.Display(80, 24)
    test_disp.set_pixel(80, 24)
    test_disp._make_frame_string() # only for test 
    assert test_disp.frame_string[-1] == '#'