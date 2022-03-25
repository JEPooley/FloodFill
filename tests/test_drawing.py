"""
test_floodfill.py: Test drawing class and flood fill algorithm.
"""

from pytest import fixture, raises
import numpy as np
from src.FloodFill.drawing import Drawing
from src.FloodFill.colours import Colours


@fixture
def simple_image():
    return np.array([
            [[255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0]],
            [[255, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0]],
            [[255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
            ])


@fixture
def binary_image():
    return np.array(
        [[1, 1, 1, 0],
         [1, 0, 1, 0],
         [1, 1, 1, 0],
         [0, 0, 0, 0]]
        ).astype(bool)


@fixture
def filled_image():
    return np.array([
            [[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0]],
            [[0, 0, 255], [0, 0, 0], [0, 0, 255], [0, 0, 0]],
            [[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
            ])


def test_get_mask(simple_image, binary_image):
    mask = Drawing.get_mask(image=simple_image, value=(255, 0, 0))
    assert np.array_equal(mask, binary_image)


def test_get_mask_error(simple_image):
    with raises(Exception) as exc_info:
        Drawing.get_mask(image=simple_image, value=(255, 0))
    assert str(exc_info.value) == "Array dimension mismatch: expected " +\
                                  "value with length 3, got 2"


def test_fill(simple_image, filled_image):
    drawing = Drawing(simple_image)
    drawing.fill(0, 0, Colours.BLUE)
    assert np.array_equal(drawing.image, filled_image)
