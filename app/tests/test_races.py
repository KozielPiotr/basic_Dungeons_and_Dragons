"""Tests for RaceName class"""

from app.characters_classes_races.character import Character
from app.characters_classes_races.races import HumanRace


class TestRaces:
    def setup_method(self):
        self.character = Character()

    def test_modify_character__abilities(self):
        """Character abilities are set to 0 by default"""
        race = HumanRace()
        character = race.modify_character(self.character)
        assert character.strength_race_bonus == race.strength_race_bonus
        assert character.condition_race_bonus == race.condition_race_bonus
        assert character.dexterity_race_bonus == race.dexterity_race_bonus
        assert character.intelligence_race_bonus == race.intelligence_race_bonus
        assert character.wisdom_race_bonus == race.wisdom_race_bonus
        assert character.charisma_race_bonus == race.charisma_race_bonus

    def test_modify_character__secondary(self):
        """Checks if attributes like size are set properly"""
        race = HumanRace()
        character = race.modify_character(self.character)
        assert character.size == race.size
        assert character.speed == race.speed
        assert character.vision == race.vision
