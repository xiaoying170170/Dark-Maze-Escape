# Dark Maze Escape

A simple terminal-based maze game where you can only see one tile around your character. Move through the maze, find keys, unlock doors, avoid traps, and try to escape!

## Features
- Randomly generated maze with a single exit
- Player can only see nearby tiles ("darkness" effect)
- Collect keys to unlock doors
- Avoid traps that reduce your health
- Breakable ice walls for added challenge

## How to Run
1. Place `main.py`, `maze.py`, and `player.py` in the same folder
2. Run the game with:

## File Overview
- `main.py`: Game entry and loop
- `maze.py`: Maze generation and map elements
- `player.py`: Player status and movement logic

## How to Play
- Use `w`, `a`, `s`, `d` keys to move up, left, down, and right
- Pick up keys (`K`) to unlock doors (`D`)
- Avoid traps (`^`) or lose health
- Break through ice walls (`*`) by moving into them
- Reach the exit (`E`) to win

---
