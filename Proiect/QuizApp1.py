import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

class QuizApp:
    def __init__(self, main_window):
        self.root = main_window
        self.root.title("Quiz App")

        # Încărcăm imaginea de fundal
        self.background_image = Image.open("Vrei_să_fii_milionar.png")  # Asigură-te că ai această imagine în același folder
        self.background_image = self.background_image.resize((800, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.background_image)

        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Încărcăm imagini cu degete mari (redimensionate la 100x100)
        self.thumb_up_img = Image.open("thumbs_up.png")  # Asigură-te că ai fișierul thumbs_up.png
        self.thumb_up_img = self.thumb_up_img.resize((200, 200), Image.Resampling.LANCZOS)
        self.thumb_up = ImageTk.PhotoImage(self.thumb_up_img)

        self.thumb_down_img = Image.open("thumbs_down.png")  # Asigură-te că ai fișierul thumbs_down.png
        self.thumb_down_img = self.thumb_down_img.resize((200, 200), Image.Resampling.LANCZOS)
        self.thumb_down = ImageTk.PhotoImage(self.thumb_down_img)

        # Lista întrebărilor
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

        # Eticheta pentru întrebări (centrată mai bine)
        self.question_label = tk.Label(self.root, text="", font=("Arial", 24, "bold"), wraplength=700, bg="white", fg="black", anchor="center")
        self.question_label.pack(pady=20)

        # Rama pentru butoane
        self.button_frame = tk.Frame(self.root, bg="black")
        self.button_frame.pack()

        # Butoane pentru opțiuni (două pe rând)
        self.options_buttons = []
        for i in range(4):
            button = tk.Button(self.button_frame, text="", font=("Arial", 16, "bold"), width=20, height=2, command=lambda i=i: self.check_answer(i))
            self.options_buttons.append(button)

        # Aranjarea butoanelor pe 2 coloane
        self.options_buttons[0].grid(row=0, column=0, padx=10, pady=10)
        self.options_buttons[1].grid(row=0, column=1, padx=10, pady=10)
        self.options_buttons[2].grid(row=1, column=0, padx=10, pady=10)
        self.options_buttons[3].grid(row=1, column=1, padx=10, pady=10)

        # Încărcăm prima întrebare
        self.load_question()

        # Label pentru degetul mare
        self.thumb_label = tk.Label(self.root)
        self.thumb_label.pack(pady=20)

        # Buton de reset
        self.reset_button = tk.Button(self.root, text="Resetează jocul", font=("Arial", 16), command=self.reset_game)
        self.reset_button.pack(pady=20)

    def load_question(self):
        # Încărcăm întrebarea curentă
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])

        for i in range(4):
            self.options_buttons[i].config(text=question_data["options"][i], state="normal", bg="lightblue", fg="black")

    def check_answer(self, selected_option):
        # Verificăm răspunsul dat de utilizator
        correct_answer = self.questions[self.current_question]["answer"]

        # Resetează fundalul la culoarea inițială
        for btn in self.options_buttons:
            btn.config(bg="lightblue")  # Resetăm culoarea fundalului opțiunilor

        # Verificăm dacă răspunsul este corect
        if selected_option == correct_answer:
            self.score += 1
            self.options_buttons[selected_option].config(bg="lightgreen", fg="black")  # Răspuns corect
            self.thumb_label.config(image=self.thumb_up)  # Arătăm degetul sus
        else:
            # Răspuns greșit
            self.options_buttons[selected_option].config(bg="lightcoral", fg="black")  # Răspuns greșit
            # Răspunsul corect
            correct_option = self.questions[self.current_question]["options"][correct_answer]
            self.options_buttons[correct_answer].config(bg="lightgreen", fg="black")  # Răspuns corect
            self.thumb_label.config(image=self.thumb_down)  # Arătăm degetul jos

        # Ștergem imaginea cu degetul după 1 secundă
        self.root.after(1000, self.clear_thumb_image)

        # Trecem la următoarea întrebare după 1 secundă
        self.root.after(1000, self.next_question)

    def clear_thumb_image(self):
        # Ștergem imaginea degetului
        self.thumb_label.config(image="")

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        # Afișăm scorul final cu imagine
        self.clear_window()

        if self.score == len(self.questions):
            image_path = "trofeu.webp"  # Imagine pentru scor perfect
            message = "Felicitări! Ești un câștigător!"
            text_color = "black"
        elif self.score >= len(self.questions) // 2:
            image_path = "mai incearca.jpg"  # Imagine pentru scor mediu
            message = "Mai exersează! Poți face mai bine data viitoare!"
            text_color = "darkblue"
        else:
            image_path = "ai pierdut 1.webp"  # Imagine pentru scor mic
            message = "Mai exersează! Ai pierdut de data aceasta."
            text_color = "black"

        # Creăm un Canvas pentru imagine și text
        canvas = tk.Canvas(self.root, width=800, height=100)
        canvas.pack(fill="both", expand=True)

        # Afișăm imaginea
        image = Image.open(image_path)
        image = image.resize((800, 700), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        canvas.background = photo  # Reținem referința pentru a preveni eliminarea imaginii
        canvas.create_image(0, 0, anchor="nw", image=photo)

        # Afișăm textul peste imagine
        canvas.create_text(400, 400, text=f"{message}\nScor: {self.score}/{len(self.questions)}",
                           font=("Arial", 24, "bold"), fill=text_color, anchor="center")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def reset_game(self):
        # Resetăm jocul
        self.current_question = 0
        self.score = 0
        self.thumb_label.config(image="")  # Ștergem imaginea degetului
        self.load_question()

# Creăm fereastra principală
main_window = tk.Tk()
main_window.geometry("800x600")  # Dimensiune fixă pentru fundalul cu imagine
quiz_app = QuizApp(main_window)

# Pornim aplicația
main_window.mainloop()