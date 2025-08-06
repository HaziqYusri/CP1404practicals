from datetime import date

class Project:
    """Class to represent a project."""
    def __init__(self, name, start_date, priority, cost, completion):
        self.name = name
        self.start_date = start_date  # datetime.date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost:,.2f}, "
                f"completion: {self.completion}%")

    def __lt__(self, other):
        """Sorted by priority"""
        return self.priority < other.priority

    def is_complete(self):
        return self.completion == 100

    def is_incomplete(self):
        return self.completion < 100

    def is_after(self, given_date):
        return self.start_date >= given_date
