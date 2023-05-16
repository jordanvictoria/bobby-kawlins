from .attraction import Attraction
from movements import Walking

# class PettingZoo:
#     """Docstring."""
#     def __init__(self, name):
#         self.attraction_name = name
#         self.description = "cute and fuzzy critters to cuddle"
#         self.animals = list()

#     def add_animal(self, animal):
#         """."""
#         self.animals.append(animal)

#     @property
#     def last_critter_added(self):
#         """."""
#         last_animal = self.animals[-1]
#         return f'{last_animal.name} the {last_animal.species}'


class PettingZoo(Attraction):
    """."""
    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, description):
        super().__init__(name, description)

    # Number 1: Duck typing check
    def add_animal_pythonic(self, animal):
        """."""
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
                print(f'{animal} now lives in {self.attraction_name}')
        except AttributeError as ex:
            print(f'{animal} doesn\'t like to be petted, so please do not put it in the {self.attraction_name} attraction.')

    # Number 2: Actual typing check
    def add_animal_type_check(self, animal):
        """."""
        if isinstance(animal, Walking):
            self.animals.append(animal)
            print(f'{animal} now lives in {self.attraction_name}')
        else:
            print(f'{animal} doesn\'t like to be petted, so please do not try to put it in the {self.attraction_name} attraction.')
        
