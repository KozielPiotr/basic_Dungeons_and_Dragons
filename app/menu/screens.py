# pylint: disable=import-error, unused-argument
"""Main menu"""

import os
from typing import Optional

from characters_classes_races.character import Character
from characters_classes_races.races import RACES


class Screen:
    """Creates visual menu"""

    @staticmethod
    def main_menu_screen(character: Optional[Character] = None):
        """Main menu"""
        print("Choose:")
        print("1. New character")
        print("2. Load character")
        print("3. Exit")

        return input()

    @staticmethod
    def create_character_screen(character):
        """Options for character creation"""
        print(
            f"1. Race    {character.race.name.value.center(10) if (character and character.race) else ''}"
        )
        print("2. Class")
        print(f"3. Name    {character.name.center(10) if character else ''}")
        print("4. Back")

        return input()

    @staticmethod
    def character_name_screen(character):
        """User can enter name for the character"""
        character.name = input("enter character name: ")
        return character

    @staticmethod
    def set_race_screen(character):
        """List of all races to choose"""
        choices = {}
        n = 1
        for key in RACES:
            print(f"{n}. {key}")
            choices[str(n)] = RACES[key]
            n += 1

        choice = input()
        character.set_race(choices[choice])
        return character

    def main_screen(self, screen=None, character=None):
        """Title, every other screen is beyond"""
        os.system("clear")
        screen = screen if screen else self.main_menu_screen
        print("DUNGEONS AND DRAGONS CHARACTER EDITOR\n")
        return screen(character)
