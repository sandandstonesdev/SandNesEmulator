import numpy as np
from dataclasses import dataclass

@dataclass
class PPUFrame:
    pixels: np.ndarray  # Shape: (240, 256, 3), dtype: np.uint8
    def __init__(self):
        self.pixels = np.zeros((240, 256, 3), dtype=np.uint8)

    def get(self) -> np.ndarray:
        return self.pixels