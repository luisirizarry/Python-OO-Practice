"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """Finds random words from dictionary."""
    def __init__(self, path):
        self.path = path
        self.words = self.read_file()
        print(f"{len(self.words)} words read")

    def read_file(self):
        """Read file and return list of words."""
        with open(self.path, "r") as file:
            content = file.read()
            return [word for word in content.split("\n")]
        
    def random(self):
        """Return random word."""
        from random import choice
        return choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """Special WordFinder that takes off blank lines and comments."""

    def read_file(self):
        """Read file and return list of words without blank lines and comments."""
        with open(self.path, "r") as file:
            content = file.read()
            return [word for word in content.split("\n") if word and not word.startswith("#")]