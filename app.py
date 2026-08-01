"""
Virtual Touchpad Pro
"""

import cv2

from config.constants import WINDOW_NAME

from core.camera import Camera


def main():

    camera = Camera()

    while True:

        frame = camera.read()

        if frame is None:
            break

        cv2.imshow(WINDOW_NAME, frame)

        if cv2.waitKey(1) == 27:
            break

    camera.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()