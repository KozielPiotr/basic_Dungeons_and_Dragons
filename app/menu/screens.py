"""Main menu"""

import os


class Screen:
    """Creates visual menu"""

    @staticmethod
    def main_menu_screen(character=None):
        print("\n")
        print("Choose:")
        print("1. New character")
        print("2. Load character")
        print("3. Exit")

        return input()

    @staticmethod
    def create_character_screen(character):
        print("1. Race")
        print("2. Class")
        print(f"3. Name    {character.name if character else ''}")
        print("4. Back")

        return input()

    @staticmethod
    def character_name_screen(character):
        character.name = input("enter character name: ")
        return character

    def main_screen(self, screen=None, character=None):
        os.system("clear")
        screen = screen if screen else self.main_menu_screen
        print("DUNGEONS AND DRAGONS CHARACTER EDITOR\n")
        return screen(character)
