"""Mechanisms to choose options from menues"""

from characters_classes_races.character import Character


class Trigger:
    """Allows choosing option from the menu"""

    def main_menu_trigger(self, choice):
        match choice:
            case "1":
                Character.create_character()
            case "2":
                pass
            case "3":
                pass
            case _:
                pass
