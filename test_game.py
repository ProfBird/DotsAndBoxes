"""
Quick test to verify game logic components work together.
"""
from grid import Grid
from player import Player
from game_logic import GameLogic


def test_game_logic():
    """Test the game logic components."""
    print("Testing Dots and Boxes game components...")
    
    # Create a small grid and players
    grid = Grid(3)
    player1 = Player("Alice")
    player2 = Player("Bob")
    players = [player1, player2]
    
    game_logic = GameLogic(grid, players)
    
    # Test 1: Add lines and check for square completion
    print("\nTest 1: Adding lines to form a square")
    print("Adding line (0,0) to (1,0) - Top")
    grid.add_line((0, 0), (1, 0))  # Top
    
    print("Adding line (0,0) to (0,1) - Left")
    grid.add_line((0, 0), (0, 1))  # Left
    
    print("Adding line (1,0) to (1,1) - Right")
    grid.add_line((1, 0), (1, 1))  # Right
    
    print("Adding line (0,1) to (1,1) - Bottom (should complete square)")
    grid.add_line((0, 1), (1, 1))  # Bottom - this should complete the square
    
    # This should complete a square
    squares = game_logic.check_for_squares((0, 1), (1, 1))  # Bottom
    print(f"Squares completed: {squares}")
    print(f"Completed squares list: {game_logic.completed_squares}")
    assert squares == 1, f"Should complete 1 square, but got {squares}"
    
    # Test 2: Check player scores
    print("\nTest 2: Updating player scores")
    player1.add_score(squares)
    print(f"{player1.name}: {player1.score} points")
    assert player1.score == 1, "Player 1 should have 1 point"
    
    # Test 3: Check current player
    print("\nTest 3: Current player management")
    current = game_logic.get_current_player()
    print(f"Current player: {current.name}")
    assert current == player1, "Current player should be Alice"
    
    game_logic.switch_player()
    current = game_logic.get_current_player()
    print(f"After switch: {current.name}")
    assert current == player2, "Current player should be Bob"
    
    # Test 4: Check game over condition
    print("\nTest 4: Game over detection")
    print(f"Is game over? {game_logic.is_game_over()}")
    print(f"Total squares completed: {len(game_logic.completed_squares)}")
    print(f"Max possible squares: {(grid.size - 1) ** 2}")
    
    # Display the grid
    print("\nFinal grid state:")
    grid.display(game_logic.completed_squares)
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_game_logic()
