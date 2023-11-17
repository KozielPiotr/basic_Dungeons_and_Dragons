"""Classes for available character classes and races"""

import abc

from .character import Character


class AbstractRace(abc.ABC):
    """Base class for character race with name and ability modifiers"""

    name = ""

    @staticmethod
    def modify_abilities(character):
        pass


class HumanRace(AbstractRace):
    """Humans tend toward no particular alignment. The best and the worst are found among them"""

    name = "human"

    @staticmethod
    def modify_abilities(character: Character) -> Character:
        character.strength += 2
        character.condition += 2
        character.dexterity += 2
        character.intelligence += 2
        character.wisdom += 2
        character.charisma += 2
        return character


class TieflingRace(AbstractRace):
    """
    To be greeted with stares and whispers, to suffer violence and insult on the street,
    to see mistrust and fear in every eye: this is the lot of the tiefling
    """

    name = "tiefling"

    @staticmethod
    def modify_abilities(character: Character) -> Character:
        character.intelligence += 2
        character.charisma += 2
        return character


class DragonornRace(AbstractRace):
    """
    Born of dragons, as their name proclaims, the dragonborn walk proudly through a world that greets them with
    fearful incomprehension
    """

    name = "dragonborn"

    @staticmethod
    def modify_abilities(character: Character) -> Character:
        character.strength += 2
        character.charisma += 2
        return character
