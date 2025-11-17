class Player:
    def __init__(self, name):
        """
        Initialize a player with a name and score.
        :param name: The name of the player.
        """
        self.name = name
        self.score = 0

    def add_score(self, points=1):
        """
        Add points to the player's score.
        :param points: The number of points to add (default is 1).
        """
        self.score += points

    def __str__(self):
        """
        Return a string representation of the player.
        """
        return f"{self.name}: {self.score} points"
