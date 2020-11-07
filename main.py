from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_entry = Question(question['text'], question['answer'])
    question_bank.append(new_entry)
points = 0
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    if quiz.next_question():
        points += 1
    print()
print()
print("You completed the quiz!")
print(f"User Score: {points}/{len(question_bank)}")





