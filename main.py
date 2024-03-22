from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"],
    question_answer = question["answer"]
    Object = Question(question_text, question_answer)
    question_bank.append(Object)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    anw, question = quiz.next_question()
    quiz.check_answer(value=anw, question=question)

if quiz.still_has_question() == False:
    print(f"Your total score is: {quiz.score}")
