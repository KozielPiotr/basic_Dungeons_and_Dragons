"""Tests for Character class"""

from app.characters_classes_races.character import Character
from app.characters_classes_races.races import DragonbornRace, TieflingRace


class TestCharacterAbilityScores:
    def setup_method(self):
        self.character = Character()
        self.bonus = 2

    def test_get_strength(self):
        """
        Character base abilities are set to 0 by default.
        Checks correctness of strength counting.
        """
        self.character.strength_race_bonus = self.bonus
        assert self.character.get_strength() == self.bonus

    def test_get_condition(self):
        """
        Character base abilities are set to 0 by default.
        Checks correctness of condition counting.
        """
        self.character.condition_race_bonus = self.bonus
        assert self.character.get_condition() == self.bonus

    def test_get_dexterity(self):
        """
        Character base abilities are set to 0 by default.
        Checks correctness of dexterity counting.
        """
        self.character.dexterity_race_bonus = self.bonus
        assert self.character.get_dexterity() == self.bonus

    def test_get_intelligence(self):
        """
        Character base abilities are set to 0 by default.
        Checks correctness of intelligence counting.
        """
        self.character.intelligence_race_bonus = self.bonus
        assert self.character.get_intelligence() == self.bonus

    def test_get_wisdom(self):
        """
        Character base abilities are set to 0 by default.
        Checks correctness of wisdom counting.
        """
        self.character.wisdom_race_bonus = self.bonus
        assert self.character.get_wisdom() == self.bonus

    def test_get_charisma(self):
        """
        Character base abilities are set to 0 by default.
        Checks correctness of charisma counting.
        """
        self.character.wisdom_race_bonus = self.bonus
        assert self.character.get_wisdom() == self.bonus

    class TestCharacterRace:
        """Setting race should assign race to the character and change character's race bonus abilities"""

        def setup_method(self):
            self.character = Character()
            self.bonus = 2

        def test_set_race_changes_character_race(self):
            race = TieflingRace
            self.character.set_race(race)
            assert self.character.race == race

        def test_set_race_changes_character_race_bonus_abilities(self):
            race = DragonbornRace
            self.character.set_race(race)
            assert self.character.strength_race_bonus == race().strength_race_bonus
