class Grid:
    def __init__(self, size):
        """
        Initialize the grid with the given size.
        :param size: The number of dots along one side of the grid (e.g., size=4 for a 4x4 grid).
        """
        self.size = size
        self.lines = set()  # Stores drawn lines as tuples of coordinates
        self.grid = [[(x, y) for x in range(size)] for y in range(size)]  # 2D list of dots

    def add_line(self, start, end):
        """
        Add a line between two dots if it's valid.
        :param start: Tuple (x1, y1) representing the starting dot.
        :param end: Tuple (x2, y2) representing the ending dot.
        :return: True if the line was added, False otherwise.
        """
        if self.is_valid_line(start, end):
            self.lines.add((start, end))
            return True
        return False

    def is_valid_line(self, start, end):
        """
        Check if a line between two dots is valid.
        :param start: Tuple (x1, y1) representing the starting dot.
        :param end: Tuple (x2, y2) representing the ending dot.
        :return: True if the line is valid, False otherwise.
        """
        # Ensure the start and end points are within bounds
        if not self.is_within_bounds(start) or not self.is_within_bounds(end):
            return False

        # Ensure the line is either horizontal or vertical and adjacent
        x1, y1 = start
        x2, y2 = end
        if abs(x1 - x2) + abs(y1 - y2) != 1:  # Must be adjacent
            return False

        # Ensure the line is not already drawn
        if (start, end) in self.lines or (end, start) in self.lines:
            return False

        return True

    def is_within_bounds(self, point):
        """
        Check if a point is within the grid bounds.
        :param point: Tuple (x, y) representing a dot.
        :return: True if the point is within bounds, False otherwise.
        """
        x, y = point
        return 0 <= x < self.size and 0 <= y < self.size

    def display(self, completed_squares=None):
        """
        Display the grid with dots, lines, and completed squares.
        :param completed_squares: Set of completed square coordinates (top-left corners).
        """
        if completed_squares is None:
            completed_squares = set()

        for y in range(self.size):
            # Print horizontal lines
            row = ""
            for x in range(self.size):
                row += "o"  # Dot
                if x < self.size - 1:
                    if ((x, y), (x + 1, y)) in self.lines or ((x + 1, y), (x, y)) in self.lines:
                        row += "---"  # Horizontal line
                    else:
                        row += "   "
            print(row)

            # Print vertical lines and square markers
            if y < self.size - 1:
                row = ""
                for x in range(self.size):
                    if ((x, y), (x, y + 1)) in self.lines or ((x, y + 1), (x, y)) in self.lines:
                        row += "|"  # Vertical line
                    else:
                        row += " "
                    
                    # Mark completed squares
                    if x < self.size - 1:
                        if (x, y) in completed_squares:
                            row += " X "  # Completed square
                        else:
                            row += "   "
                print(row)