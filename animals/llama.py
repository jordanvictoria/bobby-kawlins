from animal import Animal
from datetime import date
from movements import Walking


# class Llama:
#     """Docstring."""
#     def __init__(self, name, species, shift, food, chip_num):
#         self.name = name
#         self.species = species
#         self.shift = shift
#         self.date_added = date.today()
#         self.walking = True
#         self.food = food
#         self.__chip_number = chip_num

#     @property 
#     def chip_number(self):
#         return self.__chip_number 

#     @chip_number.setter 
#     def chip_number(self, number):
#         pass


#     def feed(self):
#         """Docstring."""
#         print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

#     def __str__(self):
#         """Docstring."""
#         return f"{self.name} is a {self.species}"





# Designate Llama as a child class by adding (Animal) after the class name
class Llama(Animal):
    """."""
    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift # stays on Llama because not all animals have shifts
        self.walking = True

    def feed(self):
        print(f'We sang "Rocktop" to {self.name} while she was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f'{self.name} the Llama'




