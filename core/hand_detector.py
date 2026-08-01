"""
MediaPipe Hand Detector
-----------------------

Converts MediaPipe output into clean Hand objects.
"""

from __future__ import annotations

import cv2
import mediapipe as mp

from core.hand import Hand
from core.enums import HandType
from core.landmark import Landmark
from core.bounding_box import BoundingBox
from core.finger_state import FingerState


class HandDetector:

    TIP_IDS = [4, 8, 12, 16, 20]

    def __init__(
        self,
        max_hands: int = 1,
        detection_confidence: float = 0.7,
        tracking_confidence: float = 0.7,
    ):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence,
        )

        self.drawer = mp.solutions.drawing_utils

    def detect(
        self,
        frame,
        draw: bool = True,
    ) -> list[Hand]:

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb)

        detected_hands: list[Hand] = []

        if not results.multi_hand_landmarks:
            return detected_hands

        h, w, _ = frame.shape

        for hand_index, hand_landmarks in enumerate(results.multi_hand_landmarks):

            hand = Hand()

            # -----------------------
            # Hand Type
            # -----------------------

            if results.multi_handedness:

                label = (
                    results.multi_handedness[hand_index]
                    .classification[0]
                    .label
                )

                if label == "Right":
                    hand.type = HandType.RIGHT

                elif label == "Left":
                    hand.type = HandType.LEFT

                else:
                    hand.type = HandType.UNKNOWN

            # -----------------------
            # Landmarks
            # -----------------------

            xs = []
            ys = []

            for idx, lm in enumerate(hand_landmarks.landmark):

                x = int(lm.x * w)
                y = int(lm.y * h)

                xs.append(x)
                ys.append(y)

                hand.landmarks.append(
                    Landmark(
                        id=idx,
                        x=x,
                        y=y,
                        z=lm.z,
                    )
                )

            # -----------------------
            # Bounding Box
            # -----------------------

            hand.bbox = BoundingBox(
                left=min(xs),
                top=min(ys),
                right=max(xs),
                bottom=max(ys),
            )

            # -----------------------
            # Finger State
            # -----------------------

            hand.fingers = self._calculate_fingers(hand)

            detected_hands.append(hand)

            # -----------------------
            # Draw
            # -----------------------

            if draw:

                self.drawer.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                )

                cv2.rectangle(
                    frame,
                    (
                        hand.bbox.left - 20,
                        hand.bbox.top - 20,
                    ),
                    (
                        hand.bbox.right + 20,
                        hand.bbox.bottom + 20,
                    ),
                    (0, 255, 0),
                    2,
                )

                cv2.putText(
                    frame,
                    hand.type.name,
                    (
                        hand.bbox.left,
                        hand.bbox.top - 25,
                    ),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 0),
                    2,
                )

        return detected_hands

    def _calculate_fingers(
        self,
        hand: Hand,
    ) -> FingerState:

        fingers = FingerState()

        lm = hand.landmarks

        # Thumb

        if hand.type == HandType.RIGHT:

            fingers.thumb = lm[4].x > lm[3].x

        else:

            fingers.thumb = lm[4].x < lm[3].x

        # Other Fingers

        fingers.index = lm[8].y < lm[6].y
        fingers.middle = lm[12].y < lm[10].y
        fingers.ring = lm[16].y < lm[14].y
        fingers.pinky = lm[20].y < lm[18].y

        return fingers

    @staticmethod
    def distance(
        p1: Landmark,
        p2: Landmark,
    ) -> float:

        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def close(self):

        self.hands.close()