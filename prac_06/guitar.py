"""
Guitar
Estimate: 20 minutes
Actual:    minutes
"""

class Guitar:
    """Represents the guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialising guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of the guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return how old the guitar is in years."""
        CURRENT_YEAR = 2022
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age() >= 50