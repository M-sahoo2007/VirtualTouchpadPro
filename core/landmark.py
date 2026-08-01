"""
Landmark model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Landmark:
    """
    Represents one MediaPipe landmark.
    """

    id: int

    x: int

    y: int

    z: float

    visibility: float = 1.0