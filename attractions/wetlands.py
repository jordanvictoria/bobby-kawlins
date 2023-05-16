class Wetlands:
    """Docstring."""
    def __init__(self, name):
        self.attraction_name = name
        self.description = "just keep swimmin"
        self.animals = list()

    def add_animal(self, animal):
        """."""
        self.animals.append(animal)