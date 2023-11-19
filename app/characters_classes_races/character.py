"""Character card"""

from typing_extensions import Self

from .races import RaceType


class Character:
    """Data from character card"""

    def __init__(self):
        self.name = ""
        self.race = None
        self.initiative = 0
        self.speed = 0
        self.size = None

        #  ability scores
        self.base_strength = 0
        self.base_condition = 0
        self.base_dexterity = 0
        self.base_intelligence = 0
        self.base_wisdom = 0
        self.base_charisma = 0

        #  defenses
        self.armor_class = 0
        self.fortitude = 0
        self.reflex = 0
        self.will = 0

        #  senses
        self.basic_insight = 10
        self.passive_perception = 10
        self.vision = None
        self.max_hp = 0

        #  hp and healing
        current_hp = 0
        self.bloodied = self.count_bloodied(current_hp)
        self.surge_value = current_hp / 4
        self.surges_per_day = 0

        #  race ability scores bonuses
        self.strength_race_bonus = 0
        self.condition_race_bonus = 0
        self.dexterity_race_bonus = 0
        self.intelligence_race_bonus = 0
        self.wisdom_race_bonus = 0
        self.charisma_race_bonus = 0

    @staticmethod
    def count_bloodied(current_hp: int) -> int:
        """Returns amount of HP, when character is bloodied"""
        return current_hp / 2

    @staticmethod
    def count_surge_value(current_hp: int) -> int:
        """Returns value of surge"""
        return current_hp / 4

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
        return self

    def set_race(self, race):
        """Sets character's race"""
        character = self.modify_character(race)
        character.race = race

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

    @classmethod
    def create_character(cls):
        """Creates new Character class"""
        new_character = cls()
        return new_character
