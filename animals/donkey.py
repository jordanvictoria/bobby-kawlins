from datetime import date
class Donkey:
    """Docstring."""
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True

mister = Donkey("Mister", "donkey", "midday")