import random

#random integer
ran_integer = random.randint(1, 100)
print(ran_integer)

#random float
ran_float = random.random()
print(ran_float)

#random float between x and y (in this case 0 and 100)
ran_float2 = random.random() * 100
print(ran_float2)

#pause 1
if random.randint(0, 1) == 0:
    print('Heads')
else:
    print('tails')