import unittest
from grid import Grid

class TestGrid(unittest.TestCase):
    def setUp(self):
        """
        Set up a grid instance for testing.
        """
        self.grid = Grid(size=4)

    def test_add_valid_line(self):
        """
        Test adding a valid line between two adjacent dots.
        """
        result = self.grid.add_line((0, 0), (0, 1))  # Vertical line
        self.assertTrue(result)
        self.assertIn(((0, 0), (0, 1)), self.grid.lines)

    def test_add_invalid_line_non_adjacent(self):
        """
        Test adding a line between two non-adjacent dots.
        """
        result = self.grid.add_line((0, 0), (1, 1))  # Non-adjacent
        self.assertFalse(result)
        self.assertNotIn(((0, 0), (1, 1)), self.grid.lines)

    def test_add_invalid_line_out_of_bounds(self):
        """
        Test adding a line where one or both dots are out of bounds.
        """
        result = self.grid.add_line((0, 0), (0, -1))  # Out of bounds
        self.assertFalse(result)
        self.assertNotIn(((0, 0), (0, -1)), self.grid.lines)

    def test_add_duplicate_line(self):
        """
        Test adding the same line twice.
        """
        self.grid.add_line((0, 0), (0, 1))  # Add the line
        result = self.grid.add_line((0, 0), (0, 1))  # Add the same line again
        self.assertFalse(result)

    def test_is_valid_line(self):
        """
        Test the is_valid_line method for various cases.
        """
        self.assertTrue(self.grid.is_valid_line((0, 0), (0, 1)))  # Valid line
        self.assertFalse(self.grid.is_valid_line((0, 0), (1, 1)))  # Non-adjacent
        self.assertFalse(self.grid.is_valid_line((0, 0), (0, -1)))  # Out of bounds
        self.grid.add_line((0, 0), (0, 1))  # Add a line
        self.assertFalse(self.grid.is_valid_line((0, 0), (0, 1)))  # Duplicate line

    def test_is_within_bounds(self):
        """
        Test the is_within_bounds method for various points.
        """
        self.assertTrue(self.grid.is_within_bounds((0, 0)))  # Within bounds
        self.assertTrue(self.grid.is_within_bounds((3, 3)))  # Edge of bounds
        self.assertFalse(self.grid.is_within_bounds((4, 4)))  # Out of bounds
        self.assertFalse(self.grid.is_within_bounds((-1, 0)))  # Negative coordinates

if __name__ == "__main__":
    unittest.main()