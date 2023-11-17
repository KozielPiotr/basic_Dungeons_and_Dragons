"""Main menu"""

import os

from .triggers import Trigger


class Screens:
    """Creates visual menu"""

    @staticmethod
    def print_menu():
        trigger = Trigger()

        print("\n")
        print("Choose:")
        print("1. New character")
        print("2. Load character")
        print("3. Exit")

        choice = input()
        trigger.main_menu_trigger(choice)

    def main_screen(self):
        os.system("clear")
        print("DUNGEONS AND DRAGONS CHARACTER EDITOR")
        self.print_menu()
