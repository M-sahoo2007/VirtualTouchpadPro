"""
Bounding box model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class BoundingBox:

    left: int

    top: int

    right: int

    bottom: int

    @property
    def width(self) -> int:
        return self.right - self.left

    @property
    def height(self) -> int:
        return self.bottom - self.top

    @property
    def center(self):

        return (
            self.left + self.width // 2,
            self.top + self.height // 2,
        )