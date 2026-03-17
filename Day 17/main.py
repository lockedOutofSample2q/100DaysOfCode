from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

to_continue = True
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
score = 0
quiz = QuizBrain(question_bank)   
while quiz.is_question_left:

    response = quiz.next_question()
    if quiz.is_correct(response):
        print("Correct answer!")
        score += 1
    else : 
        print(f"Oh! The correct answer was '{not response}'")
        print(f"Your score is:{score}")
        break
