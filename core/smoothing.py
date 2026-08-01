"""
smoothing.py

Simple cursor smoothing.
"""

from __future__ import annotations


class CursorSmoother:

    def __init__(self, factor: float = 7.0):

        self.factor = factor

        self.prev_x = 0.0
        self.prev_y = 0.0

    def smooth(
        self,
        x: float,
        y: float,
    ):

        sx = self.prev_x + (x - self.prev_x) / self.factor
        sy = self.prev_y + (y - self.prev_y) / self.factor

        self.prev_x = sx
        self.prev_y = sy

        return sx, sy