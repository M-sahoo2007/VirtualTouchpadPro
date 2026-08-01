"""
Finger state model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class FingerState:

    thumb: bool = False

    index: bool = False

    middle: bool = False

    ring: bool = False

    pinky: bool = False

    @property
    def total(self) -> int:

        return sum([
            self.thumb,
            self.index,
            self.middle,
            self.ring,
            self.pinky,
        ])

    def to_list(self):

        return [
            self.thumb,
            self.index,
            self.middle,
            self.ring,
            self.pinky,
        ]