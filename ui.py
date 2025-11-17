from grid import Grid
from player import Player
from game_logic import GameLogic


class UI:
    def __init__(self, grid, game_logic):
        """
        Initialize the UI with a grid and game logic.
        :param grid: The Grid instance.
        :param game_logic: The GameLogic instance.
        """
        self.grid = grid
        self.game_logic = game_logic

    def display_grid(self):
        """
        Display the current grid with lines and completed squares.
        """
        print("\n" + "=" * 50)
        self.grid.display(self.game_logic.completed_squares)
        print("=" * 50)

    def display_scores(self):
        """
        Display the scores for all players.
        """
        print("\nScores:")
        for player in self.game_logic.players:
            print(f"  {player}")

    def display_current_player(self):
        """
        Display whose turn it is.
        """
        player = self.game_logic.get_current_player()
        print(f"\n{player.name}'s turn!")

    def get_line_input(self):
        """
        Get user input for drawing a line.
        :return: Tuple of start and end coordinates, or None if input is invalid.
        """
        try:
            print("\nEnter coordinates to draw a line between two adjacent dots.")
            print("Format: x1,y1 x2,y2 (e.g., '0,0 0,1')")
            user_input = input("Your move: ").strip()
            
            parts = user_input.split()
            if len(parts) != 2:
                print("Invalid input. Please enter two coordinate pairs.")
                return None
            
            start = tuple(map(int, parts[0].split(',')))
            end = tuple(map(int, parts[1].split(',')))
            
            if len(start) != 2 or len(end) != 2:
                print("Invalid coordinates. Each point must have x and y values.")
                return None
            
            return start, end
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            return None

    def display_winner(self):
        """
        Display the winner of the game.
        """
        winner = self.game_logic.get_winner()
        print("\n" + "=" * 50)
        print("GAME OVER!")
        print("=" * 50)
        self.display_scores()
        print()
        if winner:
            print(f"🎉 {winner.name} wins! 🎉")
        else:
            print("It's a tie!")
        print("=" * 50)

    def display_welcome(self):
        """
        Display welcome message and game instructions.
        """
        print("\n" + "=" * 50)
        print("Welcome to Dots and Boxes!")
        print("=" * 50)
        print("\nHow to play:")
        print("- Players take turns drawing lines between adjacent dots.")
        print("- When you complete a square, you score a point and get another turn.")
        print("- The player with the most squares at the end wins!")
        print("- Enter coordinates as: x1,y1 x2,y2 (e.g., '0,0 0,1')")
        print("=" * 50)
