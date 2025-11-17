from grid import Grid
from player import Player
from game_logic import GameLogic
from ui import UI


def main():
    """
    Main function to run the Dots and Boxes game.
    """
    # Initialize UI instance (will be created later)
    ui = None

    # Welcome message
    print("\n" + "=" * 50)
    print("Welcome to Dots and Boxes!")
    print("=" * 50)

    # Get game setup from user
    try:
        grid_size = int(input("\nEnter grid size (e.g., 4 for 4x4): "))
        if grid_size < 2:
            print("Grid size must be at least 2. Setting to 4.")
            grid_size = 4
    except ValueError:
        print("Invalid input. Using default size of 4.")
        grid_size = 4

    num_players = 2  # Default to 2 players
    try:
        num_players = int(input("Enter number of players (2-4): "))
        if num_players < 2 or num_players > 4:
            print("Number of players must be between 2 and 4. Setting to 2.")
            num_players = 2
    except ValueError:
        print("Invalid input. Using 2 players.")
        num_players = 2

    # Create players
    players = []
    for i in range(num_players):
        name = input(f"Enter name for Player {i + 1}: ").strip()
        if not name:
            name = f"Player {i + 1}"
        players.append(Player(name))

    # Initialize game components
    grid = Grid(grid_size)
    game_logic = GameLogic(grid, players)
    ui = UI(grid, game_logic)

    # Display welcome and instructions
    ui.display_welcome()

    # Main game loop
    while not game_logic.is_game_over():
        ui.display_grid()
        ui.display_scores()
        ui.display_current_player()

        # Get player input
        line_coords = ui.get_line_input()
        if line_coords is None:
            continue

        start, end = line_coords

        # Try to add the line
        if grid.add_line(start, end):
            # Check if squares were completed
            squares_completed = game_logic.check_for_squares(start, end)

            if squares_completed > 0:
                print(f"\n🎊 {game_logic.get_current_player().name} completed {squares_completed} square(s)!")
                game_logic.get_current_player().add_score(squares_completed)
                print("You get another turn!")
            else:
                # Switch to next player only if no squares were completed
                game_logic.switch_player()
        else:
            print("\n❌ Invalid move! That line is either already drawn, not adjacent, or out of bounds.")
            print("Try again.")

    # Game over - display results
    ui.display_grid()
    ui.display_winner()


if __name__ == "__main__":
    main()
