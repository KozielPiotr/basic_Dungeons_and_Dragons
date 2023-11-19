# pylint: disable=import-error
"""Mechanisms to choose options from menus"""

from characters_classes_races.character import Character
from menu.screens import Screen


class Trigger:
    """Allows choosing option from the menu"""

    screen = Screen()

    def main_menu_trigger(self):
        """Match for main menu options"""
        choice = self.screen.main_screen(Screen.main_menu_screen)
        match choice:
            case "1":
                character = Character.create_character()
                self.create_character_trigger(character)
            case "2":
                pass
            case "3":
                pass
            case _:
                self.main_menu_trigger()

    def create_character_trigger(self, character: Character):
        """Match for create character options"""
        choice = self.screen.main_screen(Screen.create_character_screen, character)
        match choice:
            case "1":
                self.screen.main_screen(Screen.set_race_screen, character)
                self.create_character_trigger(character)
            case "2":
                pass
            case "3":
                character = self.screen.main_screen(
                    Screen.character_name_screen, character
                )
                self.create_character_trigger(character)
            case "4":
                self.main_menu_trigger()
        return character
