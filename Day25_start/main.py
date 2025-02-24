# with open('weather_data.csv', mode='r') as file:
#    data = file.readlines()


# import csv

# open csv file in read mode
# with open('weather_data.csv', mode='r') as file:
#     cvs.reader is going to return an object with the
#     file data
#    data = csv.reader(file)
#    temperatures = []
#
#     looping through the object
#    for row in data:
#       using try except block to only pass in the
#        values that can be converted to integers
#        try:
#            append integer to temperatures list
#            temperatures.append(int(row[1]))
#        except ValueError:
#            pass

#        print(temperatures)


# import pandas library (I'm blown away by how cool this is :)
import pandas

# read the data in the csv file
# data = pandas.read_csv('weather_data.csv')
# print all of the data in the csv file
# print(data)
# print only the data in the day column
# print(data['day'])
# print(type(data))
# print(type(data['day']))

# convert csv data to a dictionary
# data_dict = data.to_dict()
# print(data_dict)

# convert the data from the csv file in the temp column to a list
# ata_temp_list = data['temp'].to_list()
# print(data_temp_list)

# get the average temperature value in the data_temp_list
# python is so cool :). a hell of a lot quicker than using for loop in
# order to loop through the entire list. hehe
# avg1 = sum(data_temp_list) / len(data_temp_list)
# or can even do this
# using mean() method from the Series class from the pandas plugin
# avg2 = data['temp'].mean()
# print(avg2)

# get and print the max value in the 'temp' series
# max_value = data['temp'].max()
# print(max_value)

# get data in the row the day is monday
# print(data[data['day'] == 'Monday'])

# get the row of data where the temp was at a maximum
# print(data[data['temp'] == max_value])

# get a hold of the data in the Monday row
# monday = data[data.day == 'Monday']
# print the condition of the day of Monday
# print(monday.condition)

# get Monday's temperature and convert it to Fahrenheit
# monday_temp_fahrenheit = (int(monday.temp) * 9 / 5) + 32
# print(monday_temp_fahrenheit)

# create our own dataframe and convert it to a csv file
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

data = pandas.DataFrame(data=data_dict)
data.to_csv('new_data.csv')
print(data)