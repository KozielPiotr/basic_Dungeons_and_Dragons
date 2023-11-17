"""Tests for Race class"""

from app.characters_classes_races.character import Character
from app.characters_classes_races.races import HumanRace


class TestRaces:
    def test_modify_abilities(self):
        """Character abilities are set to 0 by default"""

        character = Character()
        race = HumanRace()
        character = race.modify_abilities(character)
        assert character.strength_race_bonus == 2
        assert character.condition_race_bonus == 2
        assert character.dexterity_race_bonus == 2
        assert character.intelligence_race_bonus == 2
        assert character.wisdom_race_bonus == 2
        assert character.charisma_race_bonus == 2
