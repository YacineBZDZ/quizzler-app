import html

FONT_NAME = "Arial"

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.scores = 0
        self.question_list = q_list
        self.current_question = None


    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_unscape  = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_unscape}  "

        # user_answer = input(f"Q.{self.question_number}: {q_unscape} (True/False): ")
        # self.ui.canvas.itemconfig(self.ui.question_output, text=f"Q.{self.question_number}: {q_unscape} (True/False): ")
        # self.ui.canvas.grid(column=0, row=1)
        # self.check_answer(user_answer)


    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.scores += 1
            return True
        else:
            return False


