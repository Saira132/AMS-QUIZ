from tkinter import *
from tkinter import messagebox
import json, random


def whole():

    class QUIZ:

        def __init__(self, main):
            self.main = main
            main.title("AMS")
            main.geometry("1500x1000")
            main.configure(bg="cyan4")
            frame = Frame(main, width=700,height=280)
            frame.place(x=360,y=200)
            frame.grid_propagate(0)

            try:
                with open("Qs and Ans.txt", 'r') as my_file:
                    self.data = json.load(my_file)
            except:
                print("Invalid file")
                main.destroy()
                return

            if len(self.data) < 16:
                messagebox.showerror("Error", "Insufficient No. of Questions")
                main.destroy()
                return

            self.score = 0
            self.answered = 0
            self.correct = 0
            self.inst = 0
            self.marks_value = 0

            self.display = Label(frame, text="AMS QUIZ", font=("bold",15))
            self.display.place(x=280,y=20)

            self.marks_level = Label(frame)
            self.marks_level.grid(row=1, columnspan=2, padx=20, pady=10)

            self.question = Label(frame)
            self.question.place(x=150,y=68)

            self.ent_question = Entry(frame)
            self.ent_question.place(x=220,y=195)

            self.button_submit = Button(frame,bg="cyan4",fg="white", text="Submit Your Answer", command=self.check)
            self.button_submit.place(x=360,y=190)

            self.status = Label(frame)
            self.status.grid(row=4, columnspan=2, padx=20, pady=10)

            self.button_signout = Button(frame,bg="cyan4",fg="white", text="Sign Out", command=self.main.destroy)
            self.button_signout.place(x=500,y=190)

            

            self.Question()
		#This function shows random question from the file and also diplays wether the question is hard one or not according to marks distribution
		#it also displays the correct answers at the top left of the frame
        def Question(self):
            self.ent_question.focus_set()
            if self.inst == 0:
                self.question_set = random.sample(self.data,16)

            question = random.choice(self.question_set)

            self.current_question = question['question']
            self.marks_value = int(question['marks'])

            if (int(question['marks']) >= 4):

                self.marks_level.grid(row=1, columnspan=2, padx=20, pady=10)

                self.marks_level.config(text="HARD ONE!!!!!", fg="red")
            else:
                self.marks_level.grid_forget()

            self.question.config(text=self.current_question)
            self.status.config(text=f"{self.correct}/{self.answered} Correct Answer's")
            self.question_answer = question['answer']

            self.question_set.remove(question)

            print(self.question_set)
		#This function checks whether the users enters the correct answer, displays the marks and store it in a file
        def check(self):
            self.answered += 1
            if type(self.ent_question.get()) == str:
                user_answer = str(self.ent_question.get()).lower()
            else:
                user_answer = self.ent_question.get()

            if user_answer in self.question_answer:
                self.correct += 1
                self.score += self.marks_value * 1
                messagebox.showwarning("Correct", "Correct Answer")
            else:
                messagebox.showerror("Incorrect", "Incorrect Answer")

            print("Q", self.answered)
            if self.answered == 16:
                print("Q's", self.answered)
                messagebox.showwarning("MARKS", f"Quiz Ended \n MARKS: {self.score}")
                results ={"results": self.score}
                with open("user_info.txt", 'a') as xfile:
                    json.dump(results, xfile)
                self.main.destroy()
            else:
                self.inst += 1
                self.ent_question.delete(0, 'end')
                self.Question()

    root = Tk()
    gui = QUIZ(root)
    root.mainloop()


