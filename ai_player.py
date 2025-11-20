import random
from player import Player
from gemini_client import request_move

class AIPlayer(Player):
    """AI Player that uses Gemini SDK or heuristic fallback."""

    def choose_move(self, game_logic):
        valid_moves = game_logic.get_valid_moves()
        if not valid_moves:
            return None
        # Attempt Gemini move
        player_scores = {p.name: p.score for p in game_logic.players}
        lines_drawn = list(game_logic.grid.lines)
        completed_squares = list(game_logic.completed_squares)
        move = request_move(
            board_size=game_logic.grid.size,
            lines_drawn=lines_drawn,
            completed_squares=completed_squares,
            player_scores=player_scores,
            current_player=self.name,
            valid_moves=valid_moves,
        )
        if move and move in valid_moves:
            return move
        # Fallback heuristic
        return self._heuristic_move(game_logic, valid_moves)

    def _heuristic_move(self, game_logic, valid_moves):
        # 1. Moves that complete a square
        completing = []
        for (a, b) in valid_moves:
            if game_logic.will_complete_square(a, b) > 0:
                completing.append((a, b))
        if completing:
            return random.choice(completing)
        # 2. Avoid creating third side (i.e., moves that create a nearly complete square for opponent)
        safe = []
        for (a, b) in valid_moves:
            if not self._creates_third_side(game_logic, a, b):
                safe.append((a, b))
        if safe:
            return random.choice(safe)
        # 3. Any move
        return random.choice(valid_moves)

    def _creates_third_side(self, game_logic, a, b):
        # Check potential squares around the line; if adding it creates a square with exactly 3 sides (so opponent can finish), mark risky
        x1, y1 = a
        x2, y2 = b
        size = game_logic.grid.size
        potential = []
        if x1 == x2:  # vertical
            potential.append((min(x1, x2) - 1, min(y1, y2)))
            potential.append((min(x1, x2), min(y1, y2)))
        elif y1 == y2:  # horizontal
            potential.append((min(x1, x2), min(y1, y2) - 1))
            potential.append((min(x1, x2), min(y1, y2)))
        lines = set(game_logic.grid.lines)
        # consider candidate line
        lines.add((a, b))
        for sx, sy in potential:
            if sx < 0 or sy < 0 or sx >= size - 1 or sy >= size - 1:
                continue
            edges = [
                ((sx, sy), (sx + 1, sy)),
                ((sx, sy + 1), (sx + 1, sy + 1)),
                ((sx, sy), (sx, sy + 1)),
                ((sx + 1, sy), (sx + 1, sy + 1)),
            ]
            present = 0
            for e in edges:
                if e in lines or (e[1], e[0]) in lines:
                    present += 1
            if present == 3 and ((a, b) in edges or (b, a) in edges):
                return True
        return False
