from datetime import date
class OneFish:
    """Docstring."""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

Juan = OneFish("Juan", "yellowtail")