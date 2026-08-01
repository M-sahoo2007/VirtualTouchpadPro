"""
tracker.py

Tracks the previous gesture to prevent repeated actions.
"""

from __future__ import annotations

import time


class GestureTracker:

    def __init__(self, cooldown: float = 0.30) -> None:

        self._last_gesture = None
        self._last_time = 0.0
        self.cooldown = cooldown

    def ready(self, gesture) -> bool:

        now = time.time()

        if (
            gesture != self._last_gesture
            or now - self._last_time > self.cooldown
        ):

            self._last_gesture = gesture
            self._last_time = now

            return True

        return False