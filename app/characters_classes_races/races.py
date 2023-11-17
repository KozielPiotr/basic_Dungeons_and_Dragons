"""Classes for available character classes and races"""

import abc

from .character import Character


class AbstractRace(abc.ABC):
    """Base class for character race with name and ability modifiers"""

    name = ""

    @staticmethod
    def modify_abilities(character):
        pass


class Human(AbstractRace):
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
