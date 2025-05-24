# maze.py

import random

class Wall:
    def __init__(self, wall_type="normal"):
        self.wall_type = wall_type
        self.symbol = "#" if wall_type == "normal" else "*"
        self.breakable = (wall_type == "ice")

class Trap:
    def __init__(self):
        self.symbol = "^"

class Key:
    def __init__(self):
        self.symbol = "K"

class Door:
    def __init__(self):
        self.symbol = "D"

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.start = (1, 1)
        self.exit = (height-2, width-2)
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.generate_maze()

    def generate_maze(self):
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 or x == self.width-1 or y == 0 or y == self.height-1:
                    self.grid[y][x] = Wall()
                elif (y, x) == self.start or (y, x) == self.exit:
                    self.grid[y][x] = None
                else:
                    r = random.random()
                    if r < 0.12:
                        self.grid[y][x] = Wall()
                    elif r < 0.18:
                        self.grid[y][x] = Wall("ice")
                    else:
                        self.grid[y][x] = None
        # Add one key, one door, a few traps
        self.place_random(Key, 1)
        self.place_random(Door, 1)
        self.place_random(Trap, 4)

    def place_random(self, cls, n):
        empty = [(y, x) for y in range(1, self.height-1)
                         for x in range(1, self.width-1)
                         if self.grid[y][x] is None and (y, x) != self.start and (y, x) != self.exit]
        for _ in range(n):
            if empty:
                y, x = random.choice(empty)
                self.grid[y][x] = cls()
                empty.remove((y, x))

    def get_cell(self, y, x):
        if 0 <= y < self.height and 0 <= x < self.width:
            return self.grid[y][x]
        return Wall()

    def set_cell(self, y, x, obj):
        self.grid[y][x] = obj

    def display(self, player, visibility=1):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if abs(y - player.y) <= visibility and abs(x - player.x) <= visibility:
                    if (y, x) == (player.y, player.x):
                        row += "@"
                    elif (y, x) == self.exit:
                        row += "E"
                    elif self.grid[y][x]:
                        row += self.grid[y][x].symbol
                    else:
                        row += "."
                else:
                    row += " "
            print(row)
