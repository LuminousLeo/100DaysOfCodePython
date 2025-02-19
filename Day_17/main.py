class User:

    #this function is started every time a new object of this
    #specific class is created
    def __init__(self, user_id, username):
        print('New user being created...')
        #constructors for the user
        self.user_id = user_id
        self.username = username
        #when a user is created he has 0 followers (default value)
        self.followers = 0
        #when a user is created they are not following anyone
        self.following = 0

    #method (func that is inside a class) that
    #allow a user to follow another user
    #a method always needs to have the self parameter first (so that it knows what object it is)
    def follow(self, user_followed):
        #increase the number of followers of the user that got followed
        user_followed.followers += 1
        #increase the number of following of the user that started following
        self.following += 1



#building user_1 object and passing in values to the __init__ func
#for the constructors
user_1 = User('001', 'Guts')

#building user_2 object and passing in values to the __init__ func
#for the constructors
user_2 = User('002', 'Casca')
#call in follow method for user_2 to follow user_1
user_2.follow(user_1)
#print the attributes of the user_1 object
print(user_1.user_id, user_1.username, user_1.followers, user_1.following)
#print the attributes of the user_2 object
print(user_2.user_id, user_2.username, user_2.followers, user_2.following)

