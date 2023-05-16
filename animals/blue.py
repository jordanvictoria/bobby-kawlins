from datetime import date
class BlueFish:
    """Docstring."""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

Dory = BlueFish("Dory", "Blue hippo tang")