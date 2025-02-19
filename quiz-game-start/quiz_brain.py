#create quiz brain class
class QuizBrain:
    """QuizBrain(question_bank). it is a class
    and takes in a list of objects(with 'text' and 'answer' attributes.)"""


    # this function is started every time a new object of this
    # specific class is created
    def __init__(self, question_bank):
        #the following are constructors for the QuizBrain class
        #it starts in the 1st question
        self.question_number = 0
        #get the question list
        self.question_list = question_bank
        #the user's score
        self.score = 0


    #next question method
    def next_question(self):
        """next_question() asks the user the current question
        and moves on to the next question"""

        #current_question var is an object with 2 attributes 'text' and 'answer'
        current_question = self.question_list[self.question_number]
        #increase question number
        self.question_number += 1
        #get user input
        user_input = input(f'Q.{self.question_number}: {current_question.text}. (True/False)?: ')
        self.check_answer(user_input, current_question)


    #still_has_questions method
    def still_has_questions(self):
        """still_has_questions() checks if there is 1 more question to respond.
        returns True if there is and False if there is not"""

        #try to access the next item in the list
        try:
            self.question_list[self.question_number]
        #if there's not another item in the list
        except IndexError:
            return False

        #if there is another item in the list
        return True

        # IMPORTANT NOTE BELOW!!!!!!!!!!
        #cool way of doing it with a one-liner
        #return self.question_number < len(self.question_list)
        #this means that if self.question_number == 3 and self.question_list == 5
        #then it is going to return True
        #else if self.question_number == 5 and self.question_list == 3 it returns False


    def check_answer(self, user_input, current_question):
        if user_input.lower() == current_question.answer.lower():
            self.score += 1
            print('You got it right.')
            print(f'Your current score is {self.score}/{self.question_number}')
        else:
            print("That's wrong.")
            print(f'The correct answer was {current_question.answer}')
            print(f'Your current score is {self.score}/{self.question_number}')

        print('')
