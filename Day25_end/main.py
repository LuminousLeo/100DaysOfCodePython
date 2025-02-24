import pandas

# create the dictionary that is going to be converted into a csv file
data_dict = {
    'Fur Color' : [],
    'Number of Squirrels' : []
}

# read the central park csv file in the data var
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250221.csv')

# convert all the fur colors into a list and then add it as a value to the 'Fur color' key
data_dict['Fur Color'] = list(dict.fromkeys(data['Primary Fur Color']))

# remove the first item from the list since it is nan (whatever it is really)
data_dict['Fur Color'].pop(0)

# loop through all the fur colors
for i in range(len(data_dict['Fur Color'])):
    # get the current fur color
    current_fur_color = data_dict['Fur Color'][i]
    # get the number of squirrels that have the current fur color
    list_current_fur_color = len(data[data['Primary Fur Color'] == data_dict['Fur Color'][i]])
    # append that integer to the list that is the value to the key 'Number of Squirrels'
    data_dict['Number of Squirrels'].append(list_current_fur_color)

# constructing a DataFrame from my data_dict dictionary
new_data = pandas.DataFrame(data=data_dict)

# converting new_data DataFrame into a csv file
new_data.to_csv('Squirrel_Count.csv')