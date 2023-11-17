"""Character card"""


class Character:
    """Data from character card"""

    name = ""
    initiative = 0
    speed = 0

    #  ability scores
    strength = 0
    condition = 0
    dexterity = 0
    intelligence = 0
    wisdom = 0
    charisma = 0

    #  defenses
    armor_class = 0
    fortitude = 0
    reflex = 0
    will = 0

    #  senses
    basic_insight = 10
    passive_perception = 10

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
