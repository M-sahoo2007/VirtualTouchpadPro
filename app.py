"""
Virtual Touchpad Pro

Application Entry Point

Pipeline

Camera
    ↓
Hand Detector
    ↓
Gesture Engine
    ↓
Mouse Controller
"""

from __future__ import annotations

import cv2

from config.constants import WINDOW_NAME

from core.camera import Camera
from core.hand_detector import HandDetector
from core.mouse_controller import MouseController
from core.gesture_engine import GestureEngine
from core.tracker import GestureTracker

from core.enums import Gesture

from utils.logger import create_logger

logger = create_logger(__name__)


class Application:
    """
    Main Virtual Touchpad Application.
    """

    def __init__(self) -> None:

        logger.info("Initializing application...")

        self.camera = Camera()

        self.detector = HandDetector()

        self.mouse = MouseController()

        self.gesture_engine = GestureEngine()

        self.tracker = GestureTracker()

    # ----------------------------------------------------------
    # Draw Information
    # ----------------------------------------------------------

    def draw_information(
        self,
        frame,
        hand,
        gesture: Gesture,
    ) -> None:

        cv2.putText(
            frame,
            f"Hand : {hand.type.name}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2,
        )

        cv2.putText(
            frame,
            f"Gesture : {gesture.name}",
            (10, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Raised Fingers : {hand.fingers.total}",
            (10, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Index : ({hand.index_tip.x}, {hand.index_tip.y})",
            (10, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2,
        )

    # ----------------------------------------------------------
    # Gesture Handler
    # ----------------------------------------------------------

    def handle_gesture(
        self,
        gesture: Gesture,
        hand,
        frame,
    ) -> None:

        frame_height, frame_width = frame.shape[:2]

        match gesture:

            case Gesture.MOVE:

                self.mouse.move(
                    hand.index_tip.x,
                    hand.index_tip.y,
                    frame_width,
                    frame_height,
                )

            case Gesture.LEFT_CLICK:

                if self.tracker.ready(gesture):
                    self.mouse.left_click()

            case Gesture.RIGHT_CLICK:

                if self.tracker.ready(gesture):
                    self.mouse.right_click()

            case Gesture.DOUBLE_CLICK:

                if self.tracker.ready(gesture):
                    self.mouse.double_click()

            case Gesture.DRAG:

                self.mouse.start_drag()

                self.mouse.move(
                    hand.index_tip.x,
                    hand.index_tip.y,
                    frame_width,
                    frame_height,
                )

            case Gesture.SCROLL_UP:

                self.mouse.scroll_up()

            case Gesture.SCROLL_DOWN:

                self.mouse.scroll_down()

            case Gesture.PAUSE:

                self.mouse.stop_drag()

            case Gesture.NONE:

                self.mouse.stop_drag()

            case _:

                self.mouse.stop_drag()

    # ----------------------------------------------------------
    # Main Loop
    # ----------------------------------------------------------

    def run(self) -> None:

        logger.info("Application started.")

        try:

            while True:

                frame = self.camera.read()

                if frame is None:

                    logger.error("Failed to read camera frame.")

                    break

                hands = self.detector.detect(
                    frame,
                    draw=True,
                )

                if hands:

                    hand = hands[0]

                    gesture = self.gesture_engine.detect(hand)

                    self.handle_gesture(
                        gesture,
                        hand,
                        frame,
                    )

                    self.draw_information(
                        frame,
                        hand,
                        gesture,
                    )

                else:

                    self.mouse.stop_drag()

                cv2.imshow(
                    WINDOW_NAME,
                    frame,
                )

                key = cv2.waitKey(1) & 0xFF

                if key == 27:

                    logger.info("ESC pressed.")

                    break

        except KeyboardInterrupt:

            logger.warning("Interrupted by user.")

        except Exception:

            logger.exception("Unexpected application error.")

        finally:

            logger.info("Cleaning resources...")

            self.detector.close()

            self.camera.release()

            cv2.destroyAllWindows()

            logger.info("Application closed.")

    # ----------------------------------------------------------
    # Cleanup
    # ----------------------------------------------------------

    def close(self) -> None:

        self.detector.close()

        self.camera.release()

        cv2.destroyAllWindows()


def main() -> None:

    app = Application()

    app.run()


if __name__ == "__main__":
    main()