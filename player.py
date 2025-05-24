# player.py

from maze import Wall, Trap, Key, Door

class Player:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.hp = 15
        self.keys = 0

    def move(self, dy, dx, maze):
        ny, nx = self.y + dy, self.x + dx
        cell = maze.get_cell(ny, nx)
        if cell is None:
            self.y, self.x = ny, nx
            return "Moved."
        elif isinstance(cell, Key):
            self.keys += 1
            maze.set_cell(ny, nx, None)
            self.y, self.x = ny, nx
            return "You found a key!"
        elif isinstance(cell, Trap):
            self.hp -= 5
            if self.hp <= 0:
                return "You stepped on a trap and lost all your health!"
            maze.set_cell(ny, nx, None)
            self.y, self.x = ny, nx
            return "You stepped on a trap and lost 5 health!"
        elif isinstance(cell, Door):
            if self.keys > 0:
                self.keys -= 1
                maze.set_cell(ny, nx, None)
                self.y, self.x = ny, nx
                return "You unlocked and passed through the door!"
            else:
                return "The door is locked. You need a key."
        elif isinstance(cell, Wall):
            if cell.breakable:
                maze.set_cell(ny, nx, None)
                return "You broke the ice wall!"
            else:
                return "You can't walk through the wall."
        else:
            return "Can't move in that direction."

    def status(self):
        print(f"HP: {self.hp} | Keys: {self.keys}")
