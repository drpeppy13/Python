name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
# dictionary = dict(zip(name, favorite_animal))
# print(dictionary)
from itertools import izip
print dict(izip(name,favorite_animal))
