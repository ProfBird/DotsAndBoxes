import unittest
from grid import Grid
from player import Player
from ai_player import AIPlayer
from game_logic import GameLogic

class TestAI(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(3)
        self.p1 = AIPlayer("AI")
        self.p2 = Player("Human")
        self.logic = GameLogic(self.grid, [self.p1, self.p2])

    def test_get_valid_moves_initial(self):
        moves = self.logic.get_valid_moves()
        # For 3x3 dots: horizontal edges = 3*2=6, vertical edges = 2*3=6 => 12 total
        self.assertEqual(len(moves), 12)

    def test_ai_chooses_valid_move_empty(self):
        move = self.p1.choose_move(self.logic)
        self.assertIn(move, self.logic.get_valid_moves())

    def test_ai_prefers_completing_square(self):
        # Set up three sides of a square at top-left
        self.grid.add_line((0,0),(1,0))
        self.grid.add_line((0,0),(0,1))
        self.grid.add_line((1,0),(1,1))
        # Now AI should choose the completing edge (0,1)-(1,1)
        move = self.p1.choose_move(self.logic)
        self.assertEqual(move, ((0,1),(1,1)))

    def test_will_complete_square(self):
        self.grid.add_line((0,0),(1,0))
        self.grid.add_line((0,0),(0,1))
        self.grid.add_line((1,0),(1,1))
        count = self.logic.will_complete_square((0,1),(1,1))
        self.assertEqual(count, 1)

if __name__ == '__main__':
    unittest.main()
