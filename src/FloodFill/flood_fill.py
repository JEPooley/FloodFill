"""
flood_fill.py: Implement flood fill algorithm
"""
import numpy as np
from typing import Sequence


def get_mask(image: np.ndarray, value: Sequence) -> np.ndarray:
    if image.shape[-1] != len(value):
        raise ValueError("Array dimension mismatch: expected value with " +\
                         f"length {image.shape[-1]}, got {len(value)}")
    return np.all(image == value, axis=-1)
