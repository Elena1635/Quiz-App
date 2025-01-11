import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, main_window):
        self.root = main_window
        self.root.title("Quiz App")
        self.root.configure(bg="lightblue")

        self.questions = [
            {
                "question": "Care este capitala Franței?",
                "options": ["Madrid", "Paris", "Roma", "Berlin"],
                "answer": 1
            },
            {
                "question": "Care este capitala Italiei?",
                "options": ["Roma", "Paris", "Berlin", "Madrid"],
                "answer": 0
            },
            {
                "question": "Ce limbă se vorbește în Germania?",
                "options": ["Engleză", "Franceză", "Germană", "Italiană"],
                "answer": 2
            },
            {
                "question": "Ce este Python?",
                "options": ["Un animal", "Un limbaj de programare", "Un oraș", "O plantă"],
                "answer": 1
            },
            {
                "question": "Cine a scris 'Romeo și Julieta'?",
                "options": ["Shakespeare", "Dante", "Cervantes", "Hemingway"],
                "answer": 0
            }
        ]

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(main_window, text="", font=("Arial", 16), wraplength=400, bg="lightblue")
        self.question_label.pack(pady=20)

        self.options_buttons = []
        for i in range(4):
            button = tk.Button(main_window, text="", font=("Arial", 12), width=30, height=2)
            button.config(command=self.create_command(i))
            button.pack(pady=5)
            self.options_buttons.append(button)

        self.feedback_label = tk.Label(main_window, text="", font=("Arial", 24), bg="lightblue")
        self.feedback_label.pack(pady=10)

        self.reset_button = tk.Button(main_window, text="Reset", font=("Arial", 12), command=self.reset_quiz)
        self.reset_button.pack(pady=10)

        self.load_question()

    def create_command(self, i):
        def command():
            self.check_answer(i)
        return command

    def load_question(self):
        self.feedback_label.config(text="")
        question_data = self.questions[self.current_question]

        self.question_label.config(text=question_data["question"])

        for i in range(4):
            self.options_buttons[i].config(
                text=question_data["options"][i], state="normal", bg="SystemButtonFace"
            )

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["answer"]

        if selected_option == correct_answer:
            self.score += 1
            self.feedback_label.config(text="👍", fg="green")
            self.options_buttons[selected_option].config(bg="green")
        else:
            self.feedback_label.config(text="👎", fg="red")
            self.options_buttons[selected_option].config(bg="red")
            correct_option = self.questions[self.current_question]["answer"]
            self.options_buttons[correct_option].config(bg="green")

        for button in self.options_buttons:
            button.config(state="disabled")

        self.root.after(2000, self.next_question)

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        if self.score == len(self.questions):
            messagebox.showinfo("Câștigător!", f"Felicitări! Ești câștigător! Scor: {self.score} din {len(self.questions)}.")
        elif self.score > len(self.questions) // 2:
            messagebox.showinfo("Rezultat", f"Ai terminat jocul! Scorul tău este: {self.score} din {len(self.questions)}. Aproape câștigător!")
        elif self.score == 0:
            messagebox.showerror("Pierzător!", "Ai pierdut! Nu ai nimerit niciun răspuns corect.")
        else:
            messagebox.showinfo("Pierzător", f"Ai pierdut! Scorul tău este: {self.score} din {len(self.questions)}.")
        self.reset_quiz()

    def reset_quiz(self):
        self.current_question = 0
        self.score = 0
        self.load_question()

main_window = tk.Tk()
quiz_app = QuizApp(main_window)

main_window.mainloop()