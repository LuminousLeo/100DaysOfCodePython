def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
#the for loop essentially is going to do x 20 times
# 2. When is the function meant to print "You got it"?
#when i == 20
# 3. What are your assumptions about the value of i?
#the if statement is never going to be executed because the max value of i is 19 (because of range())

#pause2
def my_function2():
    for i in range(1, 20):
        if i == 19:
            print("You got it")


my_function2()
