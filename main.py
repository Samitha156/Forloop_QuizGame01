from Questions_data import question_data
from question_format import Question
from quiz_processor import QuestionProcessor

question_library = []
for data in question_data:
    new_question = data["question"]
    new_answer = data["correct_answer"]
    quiz_object = Question(new_question, new_answer)
    question_library.append(quiz_object)

quiz = QuestionProcessor(question_library)

while quiz.still_has_question():
    quiz.next_question()

print(f"You completed the test")
print(f"your final score is {quiz.score}/{quiz.question_number}")