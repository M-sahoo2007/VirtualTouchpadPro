"""
Camera module.
"""

from __future__ import annotations

import cv2

from config.settings import camera


class Camera:

    def __init__(self) -> None:

        self.cap = cv2.VideoCapture(camera.device)

        self.cap.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            camera.width,
        )

        self.cap.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            camera.height,
        )

        self.cap.set(
            cv2.CAP_PROP_FPS,
            camera.fps,
        )

    def read(self):

        success, frame = self.cap.read()

        if not success:
            return None

        return cv2.flip(frame, 1)

    def release(self):

        self.cap.release()