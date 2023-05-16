from animals import Goat, Lamb, Llama, Pony, Donkey, Duck
from attractions import PettingZoo, Wetlands, SnakePit


# roberto = Goat("Roberto", "goat", "midday")
# print(f'{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift.')

# miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow" )

# print(miss_fuzz.feed())

# print(miss_fuzz)


# varmint_village = PettingZoo("Varmint Village")

# stinky = Llama("Stinky", "goat", "afternoon", "barley hay", 123789)

# varmint_village.add_animal(stinky)

# for animal in varmint_village.animals:
#     print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

# petty_zoo = PettingZoo("Petty Zoo")
# cutie = Llama("Cutie", "llama", "midday", "grass", 123765)

# petty_zoo.add_animal(stinky)
# petty_zoo.add_animal(cutie)

# print(petty_zoo.last_critter_added)





# bob = Duck("Bob", "Duck", "watercress sandwiches", 123735)
# bob.run()
# bob.swim()

# bob = Duck("Bob", "duck", "watercress sandwiches", 345987)

# # Create an attraction
# varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scurry")
# varmint_village.add_animal(bob)

# for animal in varmint_village.animals:
#     print(animal)



varmint_village = PettingZoo("The Varmint Village", "critters that love to be pet!")

# remember, some animals may require more arguments than others; e.g. shift
dolly = Llama("Dolly", "miniature llama", "morning", "hay", 1033)
snappy = Duck("Snappy", "American Alligator", "fish", 1044)

varmint_village.add_animal_pythonic(dolly)
varmint_village.add_animal_type_check(dolly)
varmint_village.add_animal_pythonic(snappy)

for animal in varmint_village.animals:
    print(animal)
