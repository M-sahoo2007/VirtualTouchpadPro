"""
mouse_controller.py
-------------------

Provides a high-level interface for controlling the system mouse.

Features
--------
- Smooth cursor movement
- Left click
- Right click
- Double click
- Drag & Drop
- Vertical scrolling
- Fail-safe protection
"""

from __future__ import annotations

import time
from dataclasses import dataclass

import numpy as np
import pyautogui

from config.settings import mouse


pyautogui.FAILSAFE = True


@dataclass(slots=True)
class CursorPosition:
    """Represents a cursor position on the screen."""

    x: float
    y: float


class MouseController:
    """Controls the operating system mouse."""

    def __init__(self) -> None:

        self.screen_width, self.screen_height = pyautogui.size()

        self._previous = CursorPosition(0.0, 0.0)

        self._dragging = False

        self._last_click = 0.0

        self._click_delay = 0.30

    # ---------------------------------------------------------
    # Cursor Movement
    # ---------------------------------------------------------

    def move(
        self,
        x: int,
        y: int,
        frame_width: int,
        frame_height: int,
    ) -> None:
        """
        Move the mouse cursor smoothly.

        Args:
            x: Camera x-coordinate
            y: Camera y-coordinate
            frame_width: Camera frame width
            frame_height: Camera frame height
        """

        margin = mouse.margin

        screen_x = np.interp(
            x,
            (margin, frame_width - margin),
            (0, self.screen_width),
        )

        screen_y = np.interp(
            y,
            (margin, frame_height - margin),
            (0, self.screen_height),
        )

        smooth_x = (
            self._previous.x
            + (screen_x - self._previous.x)
            / mouse.smoothing
        )

        smooth_y = (
            self._previous.y
            + (screen_y - self._previous.y)
            / mouse.smoothing
        )

        pyautogui.moveTo(smooth_x, smooth_y)

        self._previous = CursorPosition(
            smooth_x,
            smooth_y,
        )

    # ---------------------------------------------------------
    # Click Helpers
    # ---------------------------------------------------------

    def _can_click(self) -> bool:

        return (
            time.time() - self._last_click
            > self._click_delay
        )

    # ---------------------------------------------------------
    # Mouse Buttons
    # ---------------------------------------------------------

    def left_click(self) -> None:

        if not self._can_click():
            return

        pyautogui.click()

        self._last_click = time.time()

    def right_click(self) -> None:

        if not self._can_click():
            return

        pyautogui.rightClick()

        self._last_click = time.time()

    def double_click(self) -> None:

        if not self._can_click():
            return

        pyautogui.doubleClick()

        self._last_click = time.time()

    # ---------------------------------------------------------
    # Drag
    # ---------------------------------------------------------

    def start_drag(self) -> None:

        if self._dragging:
            return

        pyautogui.mouseDown()

        self._dragging = True

    def stop_drag(self) -> None:

        if not self._dragging:
            return

        pyautogui.mouseUp()

        self._dragging = False

    @property
    def dragging(self) -> bool:

        return self._dragging

    # ---------------------------------------------------------
    # Scroll
    # ---------------------------------------------------------

    def scroll_up(self) -> None:

        pyautogui.scroll(mouse.scroll_speed)

    def scroll_down(self) -> None:

        pyautogui.scroll(-mouse.scroll_speed)

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    def position(self) -> tuple[int, int]:
        """Return the current mouse position."""

        return pyautogui.position()