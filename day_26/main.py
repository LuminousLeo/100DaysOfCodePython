import pandas

student_dict = {
    'Students': ['Joker' , 'Panther', 'Skull'],
    'Scores': [97, 53, 26]
}


student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through rows of the data frame
for (index, row) in student_data_frame.iterrows():
    #print only the row in the students column
    print(row.Students)