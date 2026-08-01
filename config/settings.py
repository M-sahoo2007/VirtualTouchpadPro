"""
Application settings.
"""

from dataclasses import dataclass


@dataclass
class CameraSettings:
    width: int = 1280
    height: int = 720
    fps: int = 30
    device: int = 0


@dataclass
class MouseSettings:
    smoothing: int = 7
    margin: int = 100
    click_distance: int = 35
    scroll_speed: int = 80


camera = CameraSettings()
mouse = MouseSettings()