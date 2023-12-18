import time
import random

class TextBasedGame:
    def __init__(self):
        self.player_name = ""
        self.sections_explored = {
            "start": False,
            "forest": False,
            "cave": False,
            "mountain": False,
            "lake": False,
            "end": False
        }
        self.items_collected = []

    def intro(self):
        print("Welcome to the Text-Based Adventure Game!")
        self.player_name = input("Please enter your name: ")
        print(f"Hello, {self.player_name}! You find yourself at the beginning of a journey.")
        time.sleep(1)
        self.explore_section("start")

    def explore_section(self, section):
        if not self.sections_explored[section]:
            self.sections_explored[section] = True

            if section == "start":
                print("\nYou are at the start of your adventure.")
                print("There are four paths ahead: Forest, Cave, Mountain, and Lake.")
                choice = input("Which path do you want to take?: ").lower()

                if choice == "forest":
                    self.explore_section("forest")
                elif choice == "cave":
                    self.explore_section("cave")
                elif choice == "mountain":
                    self.explore_section("mountain")
                elif choice == "lake":
                    self.explore_section("lake")
                else:
                    print("Invalid choice. Please choose one of the paths.")
                    self.explore_section("start")

            elif section == "forest":
                print("\nYou enter a dense forest.")
                print("You see a shining object on the ground.")
                choice = input("Do you pick it up? (Yes/No): ").lower()

                if choice == "yes":
                    print("You picked up a magical gem!")
                    self.items_collected.append("gem")
                else:
                    print("You decided not to pick it up.")
                self.explore_section("start")

            elif section == "cave":
                print("\nYou venture into a dark cave.")
                print("There are two paths: Left or Right.")
                choice = input("Which path do you want to take?: ").lower()

                if choice == "left":
                    print("You encounter a treasure chest!")
                    time.sleep(1)
                    print("It's empty... Disappointing.")
                elif choice == "right":
                    print("You found a hidden passage leading deeper into the cave.")
                    self.explore_section("end")
                else:
                    print("Invalid choice. Please choose Left or Right.")
                    self.explore_section("cave")

            elif section == "mountain":
                print("\nYou climb a steep mountain.")
                print("You spot a rare flower.")
                choice = input("Do you try to collect it? (Yes/No): ").lower()

                if choice == "yes":
                    print("You collected the rare flower!")
                    self.items_collected.append("flower")
                else:
                    print("You left the flower undisturbed.")
                self.explore_section("start")

            elif section == "lake":
                print("\nYou arrive at a serene lake.")
                print("You see a boat by the shore.")
                choice = input("Do you take the boat across the lake? (Yes/No): ").lower()

                if choice == "yes":
                    print("You took the boat across the lake.")
                    self.explore_section("end")
                else:
                    print("You decided not to take the boat.")
                self.explore_section("start")

            elif section == "end":
                print("\nYou reached the end of your journey.")
                if "gem" in self.items_collected and "flower" in self.items_collected:
                    print("Congratulations! You collected both the gem and the rare flower, achieving a successful end to your adventure!")
                elif "gem" in self.items_collected:
                    print("You found the gem but missed the rare flower. You completed your adventure with some success.")
                elif "flower" in self.items_collected:
                    print("You found the rare flower but missed the gem. Your adventure was partially successful.")
                else:
                    print("Unfortunately, you couldn't collect any special items. Your adventure ends here.")

        else:
            print(f"You've already explored the {section}. Choose another path.")

        def explore_section(self, section):
         if not self.sections_explored[section]:
            self.sections_explored[section] = True

            if section == "start":
                print("\nYou are at the start of your adventure.")
                print("There are four paths ahead: Forest, Cave, Mountain, and Lake.")
                choice = input("Which path do you want to take?: ").lower()

                if choice == "forest":
                    self.explore_section("forest")
                elif choice == "cave":
                    self.explore_section("cave")
                elif choice == "mountain":
                    self.explore_section("mountain")
                elif choice == "lake":
                    self.explore_section("lake")
                else:
                    print("Invalid choice. Please choose one of the paths.")
                    self.explore_section("start")

    def play(self):
        self.intro()

# Run the game
game = TextBasedGame()
game.play()
