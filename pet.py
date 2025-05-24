# pet.py
# VirtualPet class definition

import random
import time
from utils import print_line

class VirtualPet:
    def __init__(self, name):
        self.name = name                # Pet's name
        self.hunger = 50                # Hunger: 0 (full) to 100 (starving)
        self.happiness = 50             # Happiness: 0 (sad) to 100 (happy)
        self.energy = 50                # Energy: 0 (tired) to 100 (energetic)
        self.alive = True               # Status: is pet alive

    def status(self):
        print_line()
        print(f"{self.name}'s Status:")
        print(f"Hunger:    {self.hunger}/100")
        print(f"Happiness: {self.happiness}/100")
        print(f"Energy:    {self.energy}/100")
        print_line()
        # Show current values of pet's attributes

    def feed(self):
        if self.hunger > 10:
            self.hunger -= 10
            print(f"You fed {self.name}.")
        else:
            print(f"{self.name} is not hungry right now.")
        self.energy -= 5
        self._update_mood()

    def play(self):
        if self.energy > 15:
            self.happiness += 15
            self.energy -= 15
            self.hunger += 10
            print(f"You played with {self.name}!")
        else:
            print(f"{self.name} is too tired to play.")
        self._update_mood()

    def sleep(self):
        print(f"{self.name} is sleeping...")
        time.sleep(1)
        self.energy += 25
        self.hunger += 15
        print(f"{self.name} woke up refreshed!")
        self._update_mood()

    def _update_mood(self):
        # Clamp attribute values between 0 and 100
        self.hunger = min(max(self.hunger, 0), 100)
        self.happiness = min(max(self.happiness, 0), 100)
        self.energy = min(max(self.energy, 0), 100)

        # Determine if pet is still alive
        if self.hunger >= 100:
            print(f"\nOh no! {self.name} was too hungry and ran away...")
            self.alive = False
        elif self.happiness <= 0:
            print(f"\n{self.name} is very sad and left you...")
            self.alive = False
        elif self.energy <= 0:
            print(f"\n{self.name} collapsed from exhaustion...")
            self.alive = False

    def tick(self):
        # Attribute change every round (simulate time passing)
        self.hunger += random.randint(2, 6)
        self.happiness -= random.randint(2, 5)
        self.energy -= random.randint(1, 3)
        self._update_mood()
