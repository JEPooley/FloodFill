"""
test_floodfill.py: Test flood fill algorithm
"""

from pytest import fixture
import numpy as np
import matplotlib.pyplot as plt
from FloodFill.flood_fill import get_mask


@fixture
def simple_image():
    return np.array([
        [[1, 1, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]],
        [[1, 1, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]],
        [[1, 1, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]
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
    mask = get_mask(image=simple_image, value=(1, 1, 1))
    assert np.array_equal(mask, binary_image)
