from datetime import date

class Project:
    """Class to represent a project."""
    def __init__(self, name, start_date, priority, cost, completion):
        self.name = name
        self.start_date = start_date  # datetime.date
        self.priority = priority
        self.cost = cost
        self.completion = completion

