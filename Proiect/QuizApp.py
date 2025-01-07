import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

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

        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=400)
        self.question_label.pack(pady=20)

        self.options_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 12), width=30, height=2,
                               command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.options_buttons.append(button)

        self.load_question()

    def load_question(self):
        question_data = self.questions[self.current_question]

        self.question_label.config(text=question_data["question"])

        for i in range(4):
            self.options_buttons[i].config(text=question_data["options"][i], state="normal")

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["answer"]

        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Corect!", "Răspunsul este corect!")
        else:
            correct_option = self.questions[self.current_question]["options"][correct_answer]
            messagebox.showerror("Greșit!", f"Răspunsul corect era: {correct_option}")
    
