from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def main():
    #create question_bank list that is going to
    #contain all question objects
    question_bank = []

    #loop through question_data dict
    for item in question_data:
        #create question object
        question = Question(item['question'], item['correct_answer'])
        #append question object to question bank
        question_bank.append(question)

    # note: if you print a whole object it
    # is going to give you a location in memory
    #print(question_bank[0])

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("Congratulations! You've completed the quiz.")
    print(f'Your final score was {quiz.score}/{quiz.question_number}')



main()