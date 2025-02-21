# open and read the file

with open('/Users/leona/Desktop/my_file.txt') as file:
    contents = file.read()
    print(contents)

with open('../../Desktop/my_file.txt') as file:
    contents = file.read()
    print(contents)

# open and write to the file (overwrite method)
# with open('my_file.txt', mode='w') as file2:
    # file2.write('Ahsoka Tano')

# open and write to the file (append method, or just add more content to the file)
# with open('my_file.txt', mode='a') as file2:
    # file2.write('\nHello there!')

# create and write to a new file
# with open('new_file', mode='w') as file3:
    # file3.write("It's over, Anakin. I have the high ground.")


