"""
Hand model.
"""

from dataclasses import dataclass, field

from core.enums import HandType
from core.bounding_box import BoundingBox
from core.finger_state import FingerState
from core.landmark import Landmark


@dataclass
class Hand:

    type: HandType = HandType.UNKNOWN

    landmarks: list[Landmark] = field(default_factory=list)

    bbox: BoundingBox | None = None

    fingers: FingerState = field(default_factory=FingerState)

    @property
    def wrist(self):

        return self.landmarks[0]

    @property
    def thumb_tip(self):

        return self.landmarks[4]

    @property
    def index_tip(self):

        return self.landmarks[8]

    @property
    def middle_tip(self):

        return self.landmarks[12]

    @property
    def ring_tip(self):

        return self.landmarks[16]

    @property
    def pinky_tip(self):

        return self.landmarks[20]