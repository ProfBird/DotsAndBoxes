# Copilot / AI Agent Instructions for DotsAndBoxes

Purpose: Equip AI coding agents to quickly extend, refactor, and test this small Python Dots and Boxes implementation.

## Architecture Overview
- `main.py`: Orchestrates startup (grid size, players), loops until game over. Leaves logic/UI separation intact.
- `grid.py` (`Grid`): Pure model of dots and drawn lines. Stores lines as unordered pairs of coordinate tuples in a `set`; validity = bounds + adjacency + not already present.
- `game_logic.py` (`GameLogic`): Turn management, square completion detection, winner evaluation. Squares tracked by top-left dot coordinate in `completed_squares` (a `set`). No I/O here.
- `player.py` (`Player`): Simple name + score container. `add_score()` increments numeric tally.
- `ui.py` (`UI`): All user interaction (printing grid, prompts, winner display). Parsing of moves, validation messaging. Avoid adding game logic here.
- Tests: `test.py` (unit tests for `Grid`), `test_game.py` (informal integration-style script; prints state). Use these as examples for new tests.

## Data & State Conventions
- Coordinates: `(x, y)` with `x` increasing horizontally and `y` vertically downward (0-based). Grid size N => valid coordinates `0..N-1`.
- Lines: Stored as `(start, end)` exactly as passed. Existence checks must consider both directions: `(a,b)` or `(b,a)`.
- Adjacency rule: `abs(x1 - x2) + abs(y1 - y2) == 1` (Manhattan distance). Diagonals invalid.
- Squares: Identified by top-left corner `(x, y)`. A square complete if all four edge lines present (in either direction). Max squares = `(size - 1) ** 2`.
- Turn flow: If square(s) completed, current player retains turn; else `switch_player()`.

## Control Flow (Gameplay)
1. Setup (size, players) in `main.py`.
2. Loop: UI renders -> input -> `Grid.add_line()` -> `GameLogic.check_for_squares()` -> conditional score update + potential turn switch.
3. End when all squares claimed -> winner computed.

## Extending Safely
- Keep core logic (rules, scoring, turn decisions) inside `GameLogic`; avoid mixing with I/O.
- Add new features (e.g., undo, AI player, hints) by introducing helper classes/modules rather than bloating `UI` or `main.py`.
- For AI moves: consume `grid.lines`, `game_logic.completed_squares`, and potential line candidates using `Grid.is_valid_line` without printing directly.
- For persistence (e.g., save/resume) serialize: grid size, `grid.lines`, player names/scores, `completed_squares`, current player index.

## Testing Workflow
Run unit tests:
```bash
python test.py
```
Run integration / manual scenario:
```bash
python test_game.py
```
Run discovery (add new tests under root named `test_*.py`):
```bash
python -m unittest discover
```
Add tests near existing patterns (prefer new dedicated `test_game_logic.py` for logic-only cases).

## Patterns & Style
- Minimal dependencies; keep new code dependency-free unless justified.
- Use docstrings like existing modules (brief purpose + params). Avoid inline prints in logic classes.
- Represent new internal collections as sets when uniqueness matters (mirrors `lines`, `completed_squares`).
- Input parsing is centralized in `UI.get_line_input()`; do not replicate parsing elsewhere.

## Common Pitfalls
- Forgetting bidirectional line existence check -> duplicate line acceptance bug.
- Off-by-one errors: ensure square detection excludes border squares (`x < size-1`, `y < size-1`).
- Mixing display logic with rule logic (keep separation for easier testing).
- Not awarding extra turn after multiple square completion (loop logic already supports multiple squares via returned count).

## Example: Adding an Undo Feature (Sketch)
- Track move history list of `(start, end, squares_completed, previous_player_index)`.
- Provide `GameLogic.undo_last_move()` that removes lines and squares, restores score and player index.
- Expose an `UI` command (e.g., input "undo") parsed before coordinates.

## Example: Enumerating Valid Moves
```python
valid_moves = []
for y in range(grid.size):
    for x in range(grid.size):
        for dx, dy in [(1,0),(0,1)]:
            nx, ny = x + dx, y + dy
            if nx < grid.size and ny < grid.size:
                s = (x,y); e = (nx,ny)
                if grid.is_valid_line(s, e):
                    valid_moves.append((s, e))
```

## Agent Guidance
Prioritize pure logic changes in `grid.py` / `game_logic.py` with tests first. Only modify `ui.py` for presentation or new input commands. Keep `main.py` thin. Always run tests after changes. Suggest new targeted tests when altering scoring, turn logic, or square detection.

---
Feedback welcome: Clarify areas needing more depth (AI strategy hooks, persistence, etc.).
