

class ProgrammingLanguage:
    """Represents a programming language."""

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns True if language is dynamically typed."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Returns string representation of the language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"