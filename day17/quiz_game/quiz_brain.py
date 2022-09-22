class QuizBrain():
    def __init__(self, question_bank):
        self.question_number = 0
        self.correct_answers = 0
        self.question_list = question_bank

    def next_question(self):
        question_text = self.question_list[self.question_number].text
        correct_answer = str(self.question_list[self.question_number].answer)
        self.question_number += 1
        answer = input(f"Q{self.question_number}: {question_text}. (True/False)?")
        self.check_answer(answer, correct_answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.correct_answers += 1
            print("You are right!")
        else:
            print("Opps.. You are wrong.")

    def run_quiz(self):
        while self.still_has_questions():
            self.next_question()
            print(f"{self.correct_answers}/{self.question_number} answered correctly.")

        print("You have completed the quiz!")
        print(f"Your final score is {self.correct_answers}/{self.question_number}.")

