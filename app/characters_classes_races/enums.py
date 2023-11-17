"""Enums with values for some of attributes"""

from enum import Enum


class Size(Enum):
    medium = "medium"
    large = "large"
    huge = "huge"
    gargantuan = "gargantuan"


class Vision(Enum):
    normal_vision = "normal vision"
    low_light_vision = "low-light vision"
    darkvision = "darkvision"


class RaceName(Enum):
    human = "human"
    tiefling = "tiefling"
    dragonborn = "dragonborn"
