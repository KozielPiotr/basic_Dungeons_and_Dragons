"""Classes for available character classes and races"""

from .character import Character
from .enums import RaceName, Size, Vision


class BaseRace:
    def __init__(self):
        self.name = ""

        #  abilities bonuses
        self.strength_race_bonus = 0
        self.condition_race_bonus = 0
        self.dexterity_race_bonus = 0
        self.intelligence_race_bonus = 0
        self.wisdom_race_bonus = 0
        self.charisma_race_bonus = 0

        #  secondary attributes
        self.size = None
        self.speed = 0
        self.vision = None

    def modify_character(self, character: Character) -> Character:
        character.strength_race_bonus = self.strength_race_bonus
        character.condition_race_bonus = self.condition_race_bonus
        character.dexterity_race_bonus = self.dexterity_race_bonus
        character.intelligence_race_bonus = self.intelligence_race_bonus
        character.wisdom_race_bonus = self.wisdom_race_bonus
        character.charisma_race_bonus = self.charisma_race_bonus

        character.size = self.size
        character.speed = self.speed
        character.vision = self.vision
        return character


class HumanRace(BaseRace):
    """Humans tend toward no particular alignment. The best and the worst are found among them"""

    def __init__(self):
        super().__init__()
        self.name = RaceName.human

        self.strength_race_bonus = 2
        self.condition_race_bonus = 2
        self.dexterity_race_bonus = 2
        self.intelligence_race_bonus = 2
        self.wisdom_race_bonus = 2
        self.charisma_race_bonus = 2

        self.size = Size.medium
        self.speed = 6
        self.vision = Vision.normal_vision


class TieflingRace(BaseRace):
    """
    To be greeted with stares and whispers, to suffer violence and insult on the street,
    to see mistrust and fear in every eye: this is the lot of the tiefling
    """

    def __init__(self):
        super().__init__()
        self.name = RaceName.tiefling

        self.intelligence_race_bonus = 2
        self.charisma_race_bonus = 2

        self.size = Size.medium
        self.speed = 6
        self.vision = Vision.low_light_vision


class DragonbornRace(BaseRace):
    """
    Born of dragons, as their name proclaims, the dragonborn walk proudly through a world that greets them with
    fearful incomprehension
    """

    def __init__(self):
        super().__init__()
        self.name = RaceName.dragonborn

        self.strength_race_bonus = 2
        self.charisma_race_bonus = 2

        self.size = Size.medium
        self.speed = 6
        self.vision = Vision.normal_vision


RACES = {
    RaceName.human.value: HumanRace,
    RaceName.tiefling.value: TieflingRace,
    RaceName.dragonborn.value: DragonbornRace,
}
