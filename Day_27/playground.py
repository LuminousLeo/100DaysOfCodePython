# creating a function that takes in any desired amount
# of arguments
def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(1, 5, 1, 4))


# creating a function that takes in any desired amount
# of keyword arguments
# btw **kwargs is a dictionary
def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #    print(key)
    #    print(value)

    n += kwargs['add']
    n *= kwargs['multiply']
    return n


print(calculate(n=2, add=3, multiply=5))


# create a car class
class Car:

    # takes in optional keyword arguments
    def __init__(self, **kwargs):
        self.maker = kwargs.get('maker')
        self.model = kwargs.get('model')


my_car = Car(maker='Nissan', model='GT-R R33')
print(my_car.model)