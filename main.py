# main.py
# Main program entry point

from pet import VirtualPet
from utils import input_choice, print_line
import time

def main():
    print_line()
    print("Welcome to Virtual Pet!")
    name = input("What would you like to name your pet? ")
    pet = VirtualPet(name)
    print(f"\nYou adopted {pet.name}!")

    while pet.alive:
        pet.status()
        print("What do you want to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Do nothing")
        print("5. Quit")

        choice = input_choice("Enter your choice (1-5): ", ['1','2','3','4','5'])

        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.sleep()
        elif choice == '4':
            print(f"You do nothing. Time passes...")
        elif choice == '5':
            print(f"Goodbye! {pet.name} will miss you!")
            break

        pet.tick()
        time.sleep(0.8)

    print("Game over. Thanks for playing!")

if __name__ == '__main__':
    main()
