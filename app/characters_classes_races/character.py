"""Character card"""


class Character:
    """Data from character card"""

    name = ""
    race = None
    initiative = 0
    speed = 0
    size = None

    #  ability scores
    base_strength = 0
    base_condition = 0
    base_dexterity = 0
    base_intelligence = 0
    base_wisdom = 0
    base_charisma = 0

    #  defenses
    armor_class = 0
    fortitude = 0
    reflex = 0
    will = 0

    #  senses
    basic_insight = 10
    passive_perception = 10
    vision = None

    #  hit points
    @staticmethod
    def count_bloodied(current_hp):
        return current_hp / 2

    @staticmethod
    def count_surge_value(current_hp):
        return current_hp / 4

    max_hp = 0
    current_hp = 0
    bloodied = count_bloodied(current_hp)
    surge_value = current_hp / 4
    surges_per_day = 0

    #  race ability scores bonuses
    strength_race_bonus = 0
    condition_race_bonus = 0
    dexterity_race_bonus = 0
    intelligence_race_bonus = 0
    wisdom_race_bonus = 0
    charisma_race_bonus = 0

    def set_race(self, race):
        race = race
        race().modify_character(self)
        self.race = race

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
        new_character = cls()
        return new_character
