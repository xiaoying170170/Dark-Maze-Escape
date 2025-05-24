# main.py

from maze import Maze
from player import Player

def print_line():
    print("=" * 40)

def get_input(prompt, valid=None):
    while True:
        ans = input(prompt).strip().lower()
        if valid is None or ans in valid:
            return ans
        print(f"Please enter one of {valid}.")

def clear_screen():
    print("\n" * 50)

def main():
    print_line()
    print("Welcome to the Dark Maze!")
    width, height = 12, 10
    maze = Maze(width, height)
    player = Player(*maze.start)
    steps = 0

    while True:
        clear_screen()
        maze.display(player, visibility=1)
        player.status()
        print_line()
        move = get_input("Move (w/a/s/d) or q to quit: ", ["w","a","s","d","q"])
        if move == "q":
            print("Goodbye!")
            break
        dy, dx = {"w":(-1,0), "a":(0,-1), "s":(1,0), "d":(0,1)}[move]
        result = player.move(dy, dx, maze)
        steps += 1
        print(result)
        if (player.y, player.x) == maze.exit:
            print("Congratulations! You escaped the maze!")
            print(f"Steps taken: {steps}")
            break
        if player.hp <= 0:
            print("You lost all your health. Game Over!")
            break
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()

