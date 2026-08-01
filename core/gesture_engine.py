"""
gesture_engine.py

Professional gesture recognition engine.
"""

from __future__ import annotations

from math import hypot

from core.enums import Gesture
from core.hand import Hand


class GestureEngine:
    """
    Detect gestures from a Hand object.
    """

    LEFT_CLICK_DISTANCE = 40
    RIGHT_CLICK_DISTANCE = 40

    def detect(self, hand: Hand) -> Gesture:

        fingers = hand.fingers

        thumb = hand.thumb_tip
        index = hand.index_tip
        middle = hand.middle_tip

        # ----------------------------------
        # Calculate distances
        # ----------------------------------

        thumb_index = hypot(
            thumb.x - index.x,
            thumb.y - index.y,
        )

        thumb_middle = hypot(
            thumb.x - middle.x,
            thumb.y - middle.y,
        )

        # ----------------------------------
        # Left Click
        # ----------------------------------

        if thumb_index < self.LEFT_CLICK_DISTANCE:
            return Gesture.LEFT_CLICK

        # ----------------------------------
        # Right Click
        # ----------------------------------

        if thumb_middle < self.RIGHT_CLICK_DISTANCE:
            return Gesture.RIGHT_CLICK

        # ----------------------------------
        # Move
        # ----------------------------------

        if (
            fingers.index
            and not fingers.middle
            and not fingers.ring
            and not fingers.pinky
        ):
            return Gesture.MOVE

        # ----------------------------------
        # Drag
        # ----------------------------------

        if fingers.total == 5:
            return Gesture.DRAG

        # ----------------------------------
        # Scroll
        # ----------------------------------

        if (
            fingers.index
            and fingers.middle
            and fingers.ring
        ):
            return Gesture.SCROLL_UP

        # ----------------------------------
        # Pause
        # ----------------------------------

        if fingers.total == 0:
            return Gesture.PAUSE

        return Gesture.NONE