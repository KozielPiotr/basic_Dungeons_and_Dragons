"""Main menu"""

import os


class Screen:
    """Creates visual menu"""

    @staticmethod
    def main_menu_screen():
        print("\n")
        print("Choose:")
        print("1. New character")
        print("2. Load character")
        print("3. Exit")

        return input()

    @staticmethod
    def create_character_screen():
        print("1. Race")
        print("2. Class")
        print("3. Name")
        print("4. Back")

        return input()

    @staticmethod
    def character_name_screen():
        name = input("enter character name: ")
        return name

    def main_screen(self, screen=None):
        os.system("clear")
        screen = screen if screen else self.main_menu_screen
        print("DUNGEONS AND DRAGONS CHARACTER EDITOR\n")
        return screen()
