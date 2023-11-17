"""Tests for Race class"""

from app.characters_classes_races.character import Character
from app.characters_classes_races.races import HumanRace


class TestRaces:
    def test_modify_abilities(self):
        """Character abilities are set to 0 by default"""

        character = Character()
        race = HumanRace()
        character = race.modify_abilities(character)
        assert character.strength == 2
        assert character.condition == 2
        assert character.dexterity == 2
        assert character.intelligence == 2
        assert character.wisdom == 2
        assert character.charisma == 2
