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

    #  scondary attributes
    size = None
    speed = 0
    vision = None


class HumanRace(BaseRace):
    """Humans tend toward no particular alignment. The best and the worst are found among them"""

    name = RaceName.human
    strength_race_bonus = 2
    condition_race_bonus = 2
    dexterity_race_bonus = 2
    intelligence_race_bonus = 2
    wisdom_race_bonus = 2
    charisma_race_bonus = 2
    size = Size.medium
    speed = 6
    vision = Vision.normal_vision


class TieflingRace(BaseRace):
    """
    To be greeted with stares and whispers, to suffer violence and insult on the street,
    to see mistrust and fear in every eye: this is the lot of the tiefling
    """

    name = RaceName.tiefling
    intelligence_race_bonus = 2
    charisma_race_bonus = 2
    size = Size.medium
    speed = 6
    vision = Vision.low_light_vision


class DragonbornRace(BaseRace):
    """
    Born of dragons, as their name proclaims, the dragonborn walk proudly through a world that greets them with
    fearful incomprehension
    """

    name = RaceName.dragonborn
    strength_race_bonus = 2
    charisma_race_bonus = 2
    size = Size.medium
    speed = 6
    vision = Vision.normal_vision


RACES = {
    RaceName.human.value: HumanRace,
    RaceName.tiefling.value: TieflingRace,
    RaceName.dragonborn.value: DragonbornRace,
}

RaceType = [v for v in RACES.values()]
