"""Character card"""

import math

from typing_extensions import Self

from .races import RaceType


class Character:
    """Data from character card"""

    name = ""
    race = None
    initiative = 0
    speed = 0
    size = None
    # ability scores
    base_strength = 0
    base_condition = 0
    base_dexterity = 0
    base_intelligence = 0
    base_wisdom = 0
    base_charisma = 0
    # defenses
    armor_class = 0
    fortitude = 0
    reflex = 0
    will = 0
    # senses
    basic_insight = 10
    passive_perception = 10
    vision = None
    max_hp = 0
    # hp and healing
    current_hp = 0
    surges_per_day = 0
    # race ability scores bonuses
    strength_race_bonus = 0
    condition_race_bonus = 0
    dexterity_race_bonus = 0
    intelligence_race_bonus = 0
    wisdom_race_bonus = 0
    charisma_race_bonus = 0
    # race defences bonuses
    race_armor_class_bonus = 0
    race_fortitude_bonus = 0
    race_reflex_bonus = 0
    race_will_bonus = 0

    def bloodied(self) -> int:
        """Returns amount of HP, when character is bloodied"""
        return math.floor(self.current_hp / 2)

    def surge(self) -> int:
        """Returns value of surge"""
        return math.floor(self.current_hp / 4)

    def modify_character(self, race: RaceType) -> Self:
        """Sets character's bonuses from race"""
        self.strength_race_bonus = race.strength_race_bonus
        self.condition_race_bonus = race.condition_race_bonus
        self.dexterity_race_bonus = race.dexterity_race_bonus
        self.intelligence_race_bonus = race.intelligence_race_bonus
        self.wisdom_race_bonus = race.wisdom_race_bonus
        self.charisma_race_bonus = race.charisma_race_bonus

        self.size = race.size
        self.speed = race.speed
        self.vision = race.vision

        self.race_armor_class_bonus = race.armor_class
        self.race_fortitude_bonus = race.fortitude
        self.race_reflex_bonus = race.reflex
        self.race_will_bonus = race.will
        return self

    def set_race(self, race):
        """Sets character's race"""
        character = self.modify_character(race)
        character.race = race

    # abilities
    def get_strength(self):
        """Overall strength"""
        return self.base_strength + self.strength_race_bonus

    def get_condition(self):
        """Overall condition"""
        return self.base_condition + self.condition_race_bonus

    def get_dexterity(self):
        """Overall dexterity"""
        return self.base_dexterity + self.dexterity_race_bonus

    def get_intelligence(self):
        """Overall intelligence"""
        return self.base_intelligence + self.intelligence_race_bonus

    def get_wisdom(self):
        """Overall wisdom"""
        return self.base_wisdom + self.wisdom_race_bonus

    def get_charisma(self):
        """Overall charisma"""
        return self.base_charisma + self.charisma_race_bonus

    # defences
    def get_armor_class(self):
        """Overall armor class"""
        return self.armor_class + self.race_armor_class_bonus

    def get_fortitude(self):
        """Overall fortitude"""
        return self.fortitude + self.race_fortitude_bonus

    def get_reflex(self):
        """Overall reflex"""
        return self.reflex + self.race_reflex_bonus

    def get_will(self):
        """Overall will"""
        return self.will + self.race_will_bonus

    @classmethod
    def create_character(cls):
        """Creates new Character class"""
        new_character = cls()
        return new_character
