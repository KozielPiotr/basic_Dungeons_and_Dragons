"""Main menu"""

import os


class MainMenu:
    """Creates visual menu"""

    @staticmethod
    def print_menu():
        os.system("clear")
        print("DUNGEONS AND DRAGONS CHARACTER EDITOR")
        print("\n")
        print("Choose:")
        print("1. New character")
        print("2. Load character")
        print("3. Exit")
