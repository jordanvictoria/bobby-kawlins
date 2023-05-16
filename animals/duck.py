from animal import Animal
from movements import Walking, Swimming


# class Duck:
#     """Docstring."""
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#         self.date_added = date.today()
#         self.swimming = True

# Buster = Duck("Buster", "duck")





class Duck(Animal, Swimming, Walking):
    """."""
    def __init__(self, name, species, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
        # no more self.swimming = True

    # run is defined in the Walking parent class, but also here. This run method will take precedence and Walking's run method will not be called by Goose instances
    def run(self):
        print(f'{self} waddles')

    def __str__(self):
        return f'{self.name} the Duck'


