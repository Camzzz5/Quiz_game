from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =  [Question(i["text"],i["answer"]) for i in question_data]

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():

    quiz.next_question()
    