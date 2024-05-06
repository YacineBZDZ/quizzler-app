from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"

class QuizInterface:
    def __init__(self,quiz_brain : QuizBrain ):
        self.quiz = quiz_brain
        self.question_number = 0
        self.score = 0
        # self.question_list = q_list
        self.current_question = None

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=250, height=600)
        self.window.config(padx=20, pady=20 ,bg=THEME_COLOR)

        self.label_score = Label(text="Score : 0", bg= THEME_COLOR, fg="white")
        self.label_score.grid(column=1,row=0)


        self.canvas = Canvas(width=300, height=250,bg="white")
        # self.canvas.create_image(300, 250, image= image_Bg)
        self.canvas.grid(column=0, row=2, columnspan=2,pady=50)


        self.question_output =  self.canvas.create_text(150,125,font=(FONT_NAME, 20, 'italic'),fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1)



        image_False = PhotoImage(file="images/false.png")
        self.button_true = Button(image=image_False,highlightthickness=0,bd=0, command = self.chose_True)
        self.button_true.grid(column=0, row=2)

        image_True = PhotoImage(file="images/true.png")
        self.button_false = Button(image=image_True, highlightthickness=0, bd=0, command = self.chose_False)
        self.button_false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text= f"Score: {self.quiz.scores}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_output, text=q_text)
        else:
            self.canvas.itemconfig(self.question_output, text="You've reached the end of the List")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
    def chose_True(self):

        self.give_feedback(self.quiz.check_answer("True"))

    def chose_False(self):
        self.give_feedback(self.quiz.check_answer("False"))
    def give_feedback(self, is_right):
        if is_right :
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(2000, self.get_next_question)
        # self.window.after_cancel(1000, self.canvas.config(bg="white"))

