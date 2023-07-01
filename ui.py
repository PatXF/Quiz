from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("345x500")
        self.window.configure(pady=20, padx=20, bg=THEME_COLOR)
        self.canvas = Canvas(bg="white", width=300, height=250)
        self.question = self.canvas.create_text(
            150, 120,
            text="Some random text",
            font=("Arial", 18, "italic"),
            width=280
        )
        self.canvas.grid(columnspan=2, row=1)
        self.score_label = Label()
        self.score_label.configure(text=f"Score = 0", bg=THEME_COLOR, highlightthickness=0, fg="white")
        self.score_label.grid(row=0, column=1)
        self.correct_img = PhotoImage(file="true.png")
        self.wrong_img = PhotoImage(file="false.png")
        self.correct_button = Button(
            image=self.correct_img,
            width=105,
            height=100,
            highlightthickness=0,
            command=self.c_button
        )
        self.wrong_button = Button(
            image=self.wrong_img,
            width=105,
            height=100,
            highlightthickness=0,
            command=self.w_button
        )
        self.correct_button.grid(row=3, column=1, pady=20)
        self.wrong_button.grid(row=3, column=0, pady=20)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)

    def c_button(self):
        if self.quiz.still_has_questions():
            user_answer = "true"
            self.quiz.check_answer(user_answer)
            self.get_next_question()
            self.score_label.config(text=f"Score = {self.quiz.score}")
        else:
            self.score_label.config(text="")
            self.canvas.itemconfig(self.question, text=f"Your final score is : {self.quiz.score}")

    def w_button(self):
        if self.quiz.still_has_questions():
            user_answer = "false"
            self.quiz.check_answer(user_answer)
            self.get_next_question()
        else:
            self.score_label.config(text="")
            self.canvas.itemconfig(self.question, text=f"Your final score is : {self.quiz.score}")