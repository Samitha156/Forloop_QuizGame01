class QuestionProcessor:
    def __init__(self, q_list):
        self.question_objects = q_list
        self.score = 0
        self.question_number = 0

    def still_has_question(self):
        if self.question_number < len(self.question_objects):
            return True

    def next_question(self):
        current_question = self.question_objects[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {current_question.text} (True/False) ? ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self,user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("you got it right!")
            print(f"your score is {self.score}/{self.question_number}")
        else:
            print("you are wrong!")
            print(f"your score is {self.score}/{self.question_number}")
        print(f"Correct answer is {correct_ans}")
