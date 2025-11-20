# Dots and Boxes Game

A command-line implementation of the classic Dots and Boxes game in Python.

## Game Overview

Dots and Boxes is a pencil-and-paper game for two or more players. Players take turns connecting dots on a grid to form lines. When a player completes the fourth side of a square, they score a point and get another turn. The game ends when all squares are completed, and the player with the most squares wins!

## Project Structure

```
DotsAndBoxes/
├── grid.py           # Grid and line management
├── player.py         # Player representation
├── game_logic.py     # Game rules and square detection
├── ui.py             # User interface
├── main.py           # Game entry point
├── test.py           # Unit tests for grid module
└── test_game.py      # Integration tests for game logic
```

## Module Descriptions

### `grid.py`
- Manages the grid of dots and lines
- Validates line placement (adjacency, bounds checking)
- Displays the current grid state with completed squares marked

### `player.py`
- Represents a player with a name and score
- Handles score updates

### `game_logic.py`
- Implements game rules
- Detects completed squares when lines are added
- Manages player turns
- Determines when the game is over and who wins

### `ui.py`
- Provides the command-line interface
- Displays the grid, scores, and game status
- Handles user input for drawing lines

### `main.py`
- Entry point for the game
- Initializes all components
- Runs the main game loop

## How to Play

1. Run the game:
   ```bash
   python main.py
   ```

2. Set up the game:
   - Enter the grid size (e.g., 4 for a 4x4 grid)
   - Enter the number of players (2-4)
   - Enter names for each player

3. Take turns:
   - Players enter coordinates to draw a line between two adjacent dots
   - Format: `x1,y1 x2,y2` (e.g., `0,0 0,1`)
   - If you complete a square, you get another turn!

4. Win the game:
   - The game ends when all squares are completed
   - The player with the most squares wins!

## Example Gameplay

```
Enter grid size (e.g., 4 for 4x4): 3
Enter number of players (2-4): 2
Enter name for Player 1: Alice
Enter name for Player 2: Bob

==================================================

o   o   o
         
o   o   o
         
o   o   o
==================================================

Scores:
  Alice: 0 points
  Bob: 0 points

Alice's turn!

Enter coordinates to draw a line between two adjacent dots.
Format: x1,y1 x2,y2 (e.g., '0,0 0,1')
Your move: 0,0 1,0

[Line added... continue playing...]
```

## Running Tests

### Unit Tests (Grid Module)
```bash
python test.py
```

### Integration Tests (Game Logic)
```bash
python test_game.py
```

### Run All Tests
```bash
python -m unittest discover
```

## Features

- ✅ Dynamic grid size (2x2 to any size)
- ✅ Support for 2-4 players
- ✅ Automatic square detection
- ✅ Extra turns when completing squares
- ✅ Visual display of completed squares (marked with 'X')
- ✅ Score tracking
- ✅ Input validation
- ✅ Winner determination
- ✅ Optional AI opponent (Gemini or heuristic fallback)

## Requirements

- Python 3.7 or higher
- Optional: Gemini AI opponent requires `google-generativeai` and a `GEMINI_API_KEY`.

## Game Rules

1. Players take turns drawing one line at a time
2. Lines must connect two adjacent dots (horizontally or vertically)
3. When a player completes the fourth side of a square, they:
   - Score one point
   - Get to take another turn
4. The game continues until all squares are completed
5. The player with the most squares wins
6. If tied, the game ends in a draw

## Tips for Playing

- Try to force your opponent into giving you squares
- Be careful not to give your opponent the third side of a square
- Plan ahead to create chains of squares
- The endgame often involves sacrificing squares to set up larger chains

## Game State Representation
Grid.size + Grid.lines → board geometry
GameLogic.completed_squares (which boxes are done; you may also want a mapping to the claiming player)
GameLogic.current_player_index and players (with scores)

## AI Opponent (Optional)
You can add an AI player when configuring players by typing `AI` for the player type.

### How It Chooses Moves
1. Attempts a Gemini model call (if `GEMINI_API_KEY` and dependency installed).
2. If unavailable or invalid response, falls back to heuristic:
   - Complete a square if possible.
   - Avoid creating a third side of a box (setting up opponent).
   - Otherwise choose a random valid move.

### Installing Gemini SDK
```bash
pip install google-generativeai
```

### Setting the API Key (Windows PowerShell)
```powershell
$Env:GEMINI_API_KEY = "YOUR_KEY_HERE"
```
(For permanent use, add to your profile or a .env file and load it.)

### Dynamic Prompt Contents Sent to Gemini
- Board size
- Current lines
- Completed squares
- Player scores
- Current player name
- Valid moves list (may truncate if large)

### Expected Model Output
Return exactly: `x1,y1 x2,y2` (e.g., `0,0 0,1`). Any other format triggers fallback.

### Offline / No Key
If no key or SDK missing, the AI still operates via heuristic.
