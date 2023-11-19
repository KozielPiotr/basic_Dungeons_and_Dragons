# pylint: disable=attribute-defined-outside-init, missing-function-docstring, missing-class-docstring
"""Tests for Character class"""

import pytest

from app.characters_classes_races.character import Character
from app.characters_classes_races.races import RACES

RACES = list(RACES.values())


class TestCharacterAbilityScores:
    def setup_method(self):
        self.character = Character()

    @pytest.mark.parametrize("race", RACES)
    def test_get_strength(self, race):
        """
        Character base abilities are set to 0 by default.
        Checks correctness of strength counting.
        """
        self.character.strength_race_bonus = race.strength_race_bonus
        assert self.character.get_strength() == race.strength_race_bonus

    @pytest.mark.parametrize("race", RACES)
    def test_get_condition(self, race):
        """
        Character base abilities are set to 0 by default.
        Checks correctness of condition counting.
        """
        self.character.condition_race_bonus = race.condition_race_bonus
        assert self.character.get_condition() == race.condition_race_bonus

    @pytest.mark.parametrize("race", RACES)
    def test_get_dexterity(self, race):
        """
        Character base abilities are set to 0 by default.
        Checks correctness of dexterity counting.
        """
        self.character.dexterity_race_bonus = race.dexterity_race_bonus
        assert self.character.get_dexterity() == race.dexterity_race_bonus

    @pytest.mark.parametrize("race", RACES)
    def test_get_intelligence(self, race):
        """
        Character base abilities are set to 0 by default.
        Checks correctness of intelligence counting.
        """
        self.character.intelligence_race_bonus = race.intelligence_race_bonus
        assert self.character.get_intelligence() == race.intelligence_race_bonus

    @pytest.mark.parametrize("race", RACES)
    def test_get_wisdom(self, race):
        """
        Character base abilities are set to 0 by default.
        Checks correctness of wisdom counting.
        """
        self.character.wisdom_race_bonus = race.wisdom_race_bonus
        assert self.character.get_wisdom() == race.wisdom_race_bonus

    @pytest.mark.parametrize("race", RACES)
    def test_get_charisma(self, race):
        """
        Character base abilities are set to 0 by default.
        Checks correctness of charisma counting.
        """
        self.character.charisma_race_bonus = race.charisma_race_bonus
        assert self.character.get_charisma() == race.charisma_race_bonus


class TestDefences:
    """Character base defences are set to 0 by default."""

    def setup_method(self):
        self.character = Character()

    @pytest.mark.parametrize("race", RACES)
    def test_get_armor_class(self, race):
        """Checks correctness of armor class counting."""
        self.character.race_armor_class_bonus = race.armor_class
        assert self.character.get_armor_class() == race.armor_class

    @pytest.mark.parametrize("race", RACES)
    def test_get_fortitude(self, race):
        """Checks correctness of fortitude counting."""
        self.character.race_fortitude_bonus = race.fortitude
        assert self.character.get_fortitude() == race.fortitude

    @pytest.mark.parametrize("race", RACES)
    def test_get_reflex(self, race):
        """Checks correctness of reflex counting."""
        self.character.race_reflex_bonus = race.reflex
        assert self.character.get_reflex() == race.reflex

    @pytest.mark.parametrize("race", RACES)
    def test_get_will(self, race):
        """Checks correctness of will counting."""
        self.character.race_will_bonus = race.will
        assert self.character.get_will() == race.will


class TestHealthPoints:
    """Tests methods to count HP"""

    def setup_method(self):
        self.character = Character()

    def test_bloodied(self):
        self.character.current_hp = 25
        assert self.character.bloodied() == 12

    def test_surge(self):
        self.character.current_hp = 50
        assert self.character.surge() == 12


class TestCharacterRace:
    """Setting race should assign race to the character and change character's race bonus abilities"""

    def setup_method(self):
        self.character = Character()

    @pytest.mark.parametrize("race", RACES)
    def test_set_race_changes_character_race(self, race):
        self.character.set_race(race)
        assert self.character.race == race

    @pytest.mark.parametrize("race", RACES)
    def test_set_race_changes_character_race_bonus_abilities__strength(self, race):
        self.character.set_race(race)
        assert self.character.strength_race_bonus == race.strength_race_bonus

    @pytest.mark.parametrize("race", RACES)
    def test_set_race_changes_character_race_bonus_abilities__condition(self, race):
        self.character.set_race(race)
        assert self.character.condition_race_bonus == race.condition_race_bonus

    @pytest.mark.parametrize("race", RACES)
    def test_set_race_changes_character_race_bonus_abilities__dexterity(self, race):
        self.character.set_race(race)
        assert self.character.dexterity_race_bonus == race.dexterity_race_bonus

    @pytest.mark.parametrize("race", RACES)
    def test_set_race_changes_character_race_bonus_abilities__intelligence(self, race):
        self.character.set_race(race)
        assert self.character.intelligence_race_bonus == race.intelligence_race_bonus

    @pytest.mark.parametrize("race", RACES)
    def test_set_race_changes_character_race_bonus_abilities__wisdom(self, race):
        self.character.set_race(race)
        assert self.character.wisdom_race_bonus == race.wisdom_race_bonus

    @pytest.mark.parametrize("race", RACES)
    def test_set_race_changes_character_race_bonus_abilities__charisma(self, race):
        self.character.set_race(race)
        assert self.character.charisma_race_bonus == race.charisma_race_bonus


class TestModifyCharacter:
    def setup_method(self):
        self.character = Character()

    @pytest.mark.parametrize("race", RACES)
    def test_modify_character__abilities(self, race):
        """Character abilities are set to 0 by default"""
        character = self.character.modify_character(race)
        assert character.strength_race_bonus == race.strength_race_bonus
        assert character.condition_race_bonus == race.condition_race_bonus
        assert character.dexterity_race_bonus == race.dexterity_race_bonus
        assert character.intelligence_race_bonus == race.intelligence_race_bonus
        assert character.wisdom_race_bonus == race.wisdom_race_bonus
        assert character.charisma_race_bonus == race.charisma_race_bonus

    @pytest.mark.parametrize("race", RACES)
    def test_modify_character__secondary(self, race):
        """Checks if attributes like size are set properly"""
        character = self.character.modify_character(race)
        assert character.size == race.size
        assert character.speed == race.speed
        assert character.vision == race.vision

    @pytest.mark.parametrize("race", RACES)
    def test_modify_character__defences(self, race):
        """Checks if defences are set properly"""
        character = self.character.modify_character(race)
        assert character.race_armor_class_bonus == race.armor_class
        assert character.race_fortitude_bonus == race.fortitude
        assert character.race_reflex_bonus == race.reflex
        assert character.race_will_bonus == race.will
