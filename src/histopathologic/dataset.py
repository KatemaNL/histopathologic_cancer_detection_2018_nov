import numpy as np


class Dataset:
    def __init__(self, x: np.array, y: np.array = None):
        self.x = x
        self.y = y
