"""
test_floodfill.py: Test flood fill algorithm
"""

from pytest import fixture, raises
import numpy as np
from FloodFill.flood_fill import get_mask


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


def test_binarise(simple_image, binary_image):
    mask = get_mask(image=simple_image, value=(255, 0, 0))
    assert np.array_equal(mask, binary_image)


def test_binarise_error(simple_image):
    with raises(Exception) as exc_info:
        get_mask(image=simple_image, value=(255, 0))
    assert str(exc_info.value) == "Array dimension mismatch: expected " +\
                                  "value with length 3, got 2"
