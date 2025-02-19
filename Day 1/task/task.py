#create a greeting for your program
print('Hello! This program will help you generate a name for your band with just two questions\n')
#input func automatically adds new line
#city name
city_name = input('what city did you grow up in? ')
#pet's name
pet_name = input('Whats is the name of your favorite pet? ')
#band name
band_name = city_name + ' ' + pet_name
print("Your band's name could be " + band_name)