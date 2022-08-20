from question_model import QuestionModel
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    # 注意！
    # new_question object is created as below
    # 根據QuestionModel 的格式，如果要取出question_text 與question_answer
    # 則要用 new_question.question_text 與 new_question.question_answer
    new_question = QuestionModel(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()


print("You have complete the Quiz !")
print(f"Your final is {quiz.score}/{quiz.question_number}")

