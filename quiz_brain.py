


class QuizBrain:


    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank



    def next_question(self):
        answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False): ")
        if answer == self.question_list[self.question_number].answer:
            self.question_number += 1
            print("Correct")
            return True
        else:
            self.question_number += 1
            print("Incorrect")
            return False



    def still_has_questions(self):

        return self.question_number < len(self.question_list)