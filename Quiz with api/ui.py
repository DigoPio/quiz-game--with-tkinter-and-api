from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox


THEME_COLOR = "#375362"



class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.current_score = 0
        self.messagebox = messagebox

        self.window = Tk()
        self.window.title("Quiz Brain")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=250, text=f"", font=("Arial", 18, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(bg=THEME_COLOR, highlightthickness=0, text='Score: 0', fg='white')
        self.score_label.grid(row=0, column=1)

        true_img = PhotoImage(file="Quiz with api/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        false_img = PhotoImage(file="Quiz with api/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.true_button.config(state='normal')
        self.false_button.config(state='normal')
        self.is_over()
        self.canvas.config(bg='white')
        self.score()
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text) 

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def score(self):
        self.current_score = self.quiz.score
        self.score_label.config(text=f'Score: {self.current_score}')

    def give_feedback(self, answer: bool):
        if answer:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.score()
        self.true_button.config(state='disabled')
        self.false_button.config(state='disabled')
        self.window.after(1000, self.get_next_question)

    def is_over(self):
        if not self.quiz.still_has_questions():
            user_input = self.messagebox.showinfo(title="Results", message=f'Quiz is over! You got '
                                                                           f'{self.current_score}/10 correct answers.'
                                                                           f'Thanks for playing!')
            self.window.destroy()



