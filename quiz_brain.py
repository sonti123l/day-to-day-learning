class QuizBrain:

    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self,):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        return user_answer,current_question

    def check_answer(self, value,question):
        answer = value
        que = question
        if answer == que.answer:
            self.score+=1
            print("You got it right!")
        elif answer != que.answer:
            print("You got it Wrong!")
        print(f"The correct answer was: {que.answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")

