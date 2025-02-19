import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(friends[random.randint(0, 4)])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = 'Melons'
fruits.append('Lemons')
print(fruits)
