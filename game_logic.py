class GameLogic:
    def __init__(self, grid, players):
        """
        Initialize the game logic with a grid and players.
        :param grid: The Grid instance.
        :param players: List of Player instances.
        """
        self.grid = grid
        self.players = players
        self.current_player_index = 0
        self.completed_squares = set()  # Track completed squares by top-left corner

    def get_current_player(self):
        """
        Get the current player.
        :return: The Player instance for the current player.
        """
        return self.players[self.current_player_index]

    def switch_player(self):
        """
        Switch to the next player.
        """
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def check_for_squares(self, start, end):
        """
        Check if adding a line completes any squares.
        :param start: Tuple (x1, y1) representing the starting dot.
        :param end: Tuple (x2, y2) representing the ending dot.
        :return: Number of squares completed by this line.
        """
        squares_completed = 0
        x1, y1 = start
        x2, y2 = end

        # Determine potential squares to check based on the line orientation
        potential_squares = []

        if x1 == x2:  # Vertical line
            # Check squares to the left and right
            potential_squares.append((min(x1, x2) - 1, min(y1, y2)))  # Left
            potential_squares.append((min(x1, x2), min(y1, y2)))      # Right
        elif y1 == y2:  # Horizontal line
            # Check squares above and below
            potential_squares.append((min(x1, x2), min(y1, y2) - 1))  # Above
            potential_squares.append((min(x1, x2), min(y1, y2)))      # Below

        # Check each potential square
        for top_left_x, top_left_y in potential_squares:
            if self.is_square_complete(top_left_x, top_left_y):
                if (top_left_x, top_left_y) not in self.completed_squares:
                    self.completed_squares.add((top_left_x, top_left_y))
                    squares_completed += 1

        return squares_completed

    def is_square_complete(self, x, y):
        """
        Check if a square with the given top-left corner is complete.
        :param x: X-coordinate of the top-left corner.
        :param y: Y-coordinate of the top-left corner.
        :return: True if the square is complete, False otherwise.
        """
        # Check if all four edges of the square exist
        if x < 0 or y < 0 or x >= self.grid.size - 1 or y >= self.grid.size - 1:
            return False

        # Define the four edges of the square
        top = ((x, y), (x + 1, y))
        bottom = ((x, y + 1), (x + 1, y + 1))
        left = ((x, y), (x, y + 1))
        right = ((x + 1, y), (x + 1, y + 1))

        # Check if all four edges exist in the grid
        return (self.has_line(top) and self.has_line(bottom) and 
                self.has_line(left) and self.has_line(right))

    def has_line(self, line):
        """
        Check if a line exists in the grid (in either direction).
        :param line: Tuple of two coordinates ((x1, y1), (x2, y2)).
        :return: True if the line exists, False otherwise.
        """
        return line in self.grid.lines or (line[1], line[0]) in self.grid.lines

    def is_game_over(self):
        """
        Check if the game is over (all possible squares are completed).
        :return: True if the game is over, False otherwise.
        """
        max_squares = (self.grid.size - 1) ** 2
        return len(self.completed_squares) >= max_squares

    def get_winner(self):
        """
        Get the winner of the game (player with the highest score).
        :return: The Player instance of the winner, or None if it's a tie.
        """
        if not self.is_game_over():
            return None

        max_score = max(player.score for player in self.players)
        winners = [player for player in self.players if player.score == max_score]

        if len(winners) == 1:
            return winners[0]
        else:
            return None  # Tie
