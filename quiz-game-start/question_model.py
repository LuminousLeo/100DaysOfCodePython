class Question:
    """Question(text, answer). Takes 2 arguments
    for the constructors"""

    # this function is started every time a new object of this
    # specific class is created
    def __init__(self, text, answer):
        #the following are constructors for the Question class
        #get the text
        self.text = text
        #get the answer
        self.answer = answer