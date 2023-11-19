# pylint: disable=too-few-public-methods
"""Classes for available character classes and races"""

from .enums import RaceName, Size, Vision


class BaseRace:
    """Base class for all races"""

    #  abilities bonuses
    strength_race_bonus = 0
    condition_race_bonus = 0
    dexterity_race_bonus = 0
    intelligence_race_bonus = 0
    wisdom_race_bonus = 0
    charisma_race_bonus = 0

    #  secondary attributes
    size = None
    speed = 0
    vision = None

    # defences
    armor_class = 0
    fortitude = 0
    reflex = 0
    will = 0


class HumanRace(BaseRace):
    """Humans tend toward no particular alignment. The best and the worst are found among them"""

    name = RaceName.HUMAN
    strength_race_bonus = 2
    condition_race_bonus = 2
    dexterity_race_bonus = 2
    intelligence_race_bonus = 2
    wisdom_race_bonus = 2
    charisma_race_bonus = 2

    size = Size.MEDIUM
    speed = 6
    vision = Vision.NORMAL_VISION

    fortitude = 1
    reflex = 1
    will = 1


class TieflingRace(BaseRace):
    """
    To be greeted with stares and whispers, to suffer violence and insult on the street,
    to see mistrust and fear in every eye: this is the lot of the tiefling
    """

    name = RaceName.TIEFLING
    intelligence_race_bonus = 2
    charisma_race_bonus = 2
    size = Size.MEDIUM
    speed = 6
    vision = Vision.LOW_LIGHT_VISION


class DragonbornRace(BaseRace):
    """
    Born of dragons, as their name proclaims, the Dragonborn walk proudly through a world that greets them with
    fearful incomprehension
    """

    name = RaceName.DRAGONBORN
    strength_race_bonus = 2
    charisma_race_bonus = 2
    size = Size.MEDIUM
    speed = 6
    vision = Vision.NORMAL_VISION


RACES = {
    RaceName.HUMAN.value: HumanRace,
    RaceName.TIEFLING.value: TieflingRace,
    RaceName.DRAGONBORN.value: DragonbornRace,
}

RaceType = list(RACES.values())
