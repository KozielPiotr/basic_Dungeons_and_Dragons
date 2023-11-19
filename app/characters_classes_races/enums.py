"""Enums with values for some of the attributes"""

from enum import Enum


class Size(Enum):
    """Size of a race"""

    MEDIUM = "medium"
    LARGE = "large"
    HUGE = "huge"
    GARGANTUAN = "gargantuan"


class Vision(Enum):
    """Kinds of vision. Used with every single race"""

    NORMAL_VISION = "normal vision"
    LOW_LIGHT_VISION = "low-light vision"
    DARKVISION = "darkvision"


class RaceName(Enum):
    """All implemented races names"""

    HUMAN = "Human"
    TIEFLING = "Tiefling"
    DRAGONBORN = "Dragonborn"
