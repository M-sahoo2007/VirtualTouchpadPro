"""
Application enumerations.
"""

from __future__ import annotations

from enum import Enum, auto


class HandType(Enum):
    """Detected hand."""

    LEFT = auto()
    RIGHT = auto()
    UNKNOWN = auto()


class Gesture(Enum):
    """Supported gestures."""

    NONE = auto()

    MOVE = auto()

    LEFT_CLICK = auto()

    RIGHT_CLICK = auto()

    DOUBLE_CLICK = auto()

    DRAG = auto()

    SCROLL_UP = auto()

    SCROLL_DOWN = auto()

    VOLUME = auto()

    BRIGHTNESS = auto()

    SCREENSHOT = auto()

    PAUSE = auto()