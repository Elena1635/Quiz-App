"""
import tkinter as tk
from PIL import Image, ImageTk


class QuizApp:
    def __init__(self, main_window):
        self.root = main_window
        self.root.title("Quiz App")
        # Configurăm fereastra să fie redimensionabilă
        self.root.geometry("800x600")
        # Încărcăm imaginea de fundal
        self.background_image = Image.open("Vrei_sa_fii_milionar.png")  # Asigură-te că ai această imagine în același folder
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
                "question": "Care este rezulatul calcului: 5+25:5-3?",
                "options": ["7", "3", "15", "9"],
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
        if hasattr(self, 'thumb_label') and self.thumb_label.winfo_exists():
         self.thumb_label.config(image="")

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        # Ștergem conținutul anterior
        self.clear_window()

        # Alegem imaginea și mesajul în funcție de scor
        if self.score == len(self.questions):
            image_path = "trofeu.webp"
            message = "Felicitări! Ești un câștigător!"
            text_color = "black"
        elif self.score >= len(self.questions) // 2:
            image_path = "mai incearca.jpg"
            message = "Mai exersează! Poți face mai bine data viitoare!"
            text_color = "darkblue"
        else:
            image_path = "ai pierdut.jpg"
            message = "Mai exersează! Ai pierdut de data aceasta."
            text_color = "black"

        # Creăm un canvas care ocupă toată fereastra
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill="both", expand=True)

        # Încărcăm imaginea
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_id = self.canvas.create_image(self.canvas.winfo_width() // 2,
                                                 self.canvas.winfo_height() // 2,
                                                 anchor="center", image=self.photo)

        # Afișăm textul centrat
        self.text_id = self.canvas.create_text(self.canvas.winfo_width() // 2,
                                               self.canvas.winfo_height() - 100,
                                               text=f"{message}\nScor: {self.score}/{len(self.questions)}",
                                               font=("Arial", 24, "bold"), fill=text_color, anchor="center")

        # Creăm butonul de restart
        self.restart_button = tk.Button(self.root, text="Începe din nou", font=("Arial", 16), command=self.reset_game)
        self.restart_button.pack(pady=20)
        # Asociem funcția de redimensionare
        self.canvas.bind("<Configure>", self.resize_image)

    def resize_image(self, event):
        new_width = event.width
        new_height = event.height

        # Redimensionăm imaginea păstrând proporțiile
        resized_image = self.image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(resized_image)

        # Actualizăm imaginea și textul pe canvas
        self.canvas.itemconfig(self.image_id, image=self.photo)
        self.canvas.coords(self.image_id, new_width // 2, new_height // 2)
        self.canvas.coords(self.text_id, new_width // 2, new_height - 100)

    def clear_window(self):
        for widget in self.root.winfo_children():
                widget.destroy()

    def reset_game(self):
        # Resetăm jocul
       # self.current_question = 0
       # self.score = 0
        #self.thumb_label.config(image="")  # Ștergem imaginea degetului
       # self.load_question()

        # Încărcăm prima întrebare
        #self.load_question()
            # Resetăm jocul
            self.current_question = 0
            self.score = 0

            # Verificăm dacă thumb_label există și o resetăm sau o recreăm
            if hasattr(self, 'thumb_label') and self.thumb_label.winfo_exists():
                self.thumb_label.config(image="")  # Ștergem imaginea degetului
            else:
                # Dacă thumb_label nu există, îl recreăm
                self.thumb_label = tk.Label(self.root)
                self.thumb_label.pack(pady=20)

            # Creăm din nou butoanele pentru opțiuni
            self.button_frame = tk.Frame(self.root, bg="black")
            self.button_frame.pack()

            # Butoane pentru opțiuni (două pe rând)
            self.options_buttons = []
            for i in range(4):
                button = tk.Button(self.button_frame, text="", font=("Arial", 16, "bold"), width=20, height=2,
                                   command=lambda i=i: self.check_answer(i))
                self.options_buttons.append(button)

            # Aranjarea butoanelor pe 2 coloane
            self.options_buttons[0].grid(row=0, column=0, padx=10, pady=10)
            self.options_buttons[1].grid(row=0, column=1, padx=10, pady=10)
            self.options_buttons[2].grid(row=1, column=0, padx=10, pady=10)
            self.options_buttons[3].grid(row=1, column=1, padx=10, pady=10)

            # Re-creăm label-ul pentru întrebare
            self.question_label = tk.Label(self.root, text="", font=("Arial", 24, "bold"), wraplength=700, bg="white",
                                           fg="black", anchor="center")
            self.question_label.pack(pady=20)

            # Încărcăm prima întrebare
            self.load_question()


# Creăm fereastra principală
main_window = tk.Tk()
main_window.geometry("800x600")  # Dimensiune fixă pentru fundalul cu imagine
quiz_app = QuizApp(main_window)

# Pornim aplicația
main_window.mainloop()
"""

"""
class QuizApp:
    def __init__(self, main_window):
        self.root = main_window
        self.root.title("Quiz App")
        self.root.geometry("800x600")

        # Încărcăm imaginea de fundal
        self.background_image = Image.open("Vrei_sa_fii_milionar.png")
        self.background_image = self.background_image.resize((800, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.background_image)

        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        self.thumb_up_img = Image.open("thumbs_up.png")
        self.thumb_up_img = self.thumb_up_img.resize((200, 200), Image.Resampling.LANCZOS)
        self.thumb_up = ImageTk.PhotoImage(self.thumb_up_img)

        self.thumb_down_img = Image.open("thumbs_down.png")
        self.thumb_down_img = self.thumb_down_img.resize((200, 200), Image.Resampling.LANCZOS)
        self.thumb_down = ImageTk.PhotoImage(self.thumb_down_img)

        # Lista întrebărilor
        self.questions = [
            {"question": "Care este capitala Franței?", "options": ["Madrid", "Paris", "Roma", "Berlin"], "answer": 1},
            {"question": "Care este rezulatul calcului: 5+25:5-3?", "options": ["7", "3", "15", "9"], "answer": 0},
            {"question": "Ce limbă se vorbește în Germania?", "options": ["Engleză", "Franceză", "Germană", "Italiană"], "answer": 2},
            {"question": "Ce este Python?", "options": ["Un animal", "Un limbaj de programare", "Un oraș", "O plantă"], "answer": 1},
            {"question": "Cine a scris 'Romeo și Julieta'?", "options": ["Shakespeare", "Dante", "Cervantes", "Hemingway"], "answer": 0}
        ]
        self.current_question = 0
        self.score = 0

        # Eticheta pentru întrebări
        self.question_label = tk.Label(self.root, text="", font=("Arial", 24, "bold"), wraplength=700, bg="white", fg="black", anchor="center")
        self.question_label.pack(pady=20)

        # Rama pentru butoane
        self.button_frame = tk.Frame(self.root, bg="black")
        self.button_frame.pack()

        # Butoane pentru opțiuni
        self.options_buttons = []
        for i in range(4):
            button = tk.Button(self.button_frame, text="", font=("Arial", 16, "bold"), width=20, height=2, command=lambda i=i: self.check_answer(i))
            self.options_buttons.append(button)

        self.options_buttons[0].grid(row=0, column=0, padx=10, pady=10)
        self.options_buttons[1].grid(row=0, column=1, padx=10, pady=10)
        self.options_buttons[2].grid(row=1, column=0, padx=10, pady=10)
        self.options_buttons[3].grid(row=1, column=1, padx=10, pady=10)

        self.load_question()

        # Label pentru degetul mare
        self.thumb_label = tk.Label(self.root)
        self.thumb_label.pack(pady=20)

        # Buton de reset
        self.reset_button = tk.Button(self.root, text="Resetează jocul", font=("Arial", 16), command=self.reset_game)
        self.reset_button.pack(pady=20)

    def load_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])

        for i in range(4):
            self.options_buttons[i].config(text=question_data["options"][i], state="normal", bg="lightblue", fg="black")

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["answer"]

        for btn in self.options_buttons:
            btn.config(bg="lightblue")

        if selected_option == correct_answer:
            self.score += 1
            self.options_buttons[selected_option].config(bg="lightgreen", fg="black")
            self.thumb_label.config(image=self.thumb_up)
        else:
            self.options_buttons[selected_option].config(bg="lightcoral", fg="black")
            correct_option = self.questions[self.current_question]["options"][correct_answer]
            self.options_buttons[correct_answer].config(bg="lightgreen", fg="black")
            self.thumb_label.config(image=self.thumb_down)

        self.root.after(1000, self.clear_thumb_image)
        self.root.after(1000, self.next_question)

    def clear_thumb_image(self):
        self.thumb_label.config(image="")

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        self.clear_window()

        if self.score == len(self.questions):
            image_path = "trofeu.webp"
            message = "Felicitări! Ești un câștigător!"
        elif self.score >= len(self.questions) // 2:
            image_path = "mai incearca.jpg"
            message = "Mai exersează! Poți face mai bine data viitoare!"
        else:
            image_path = "ai pierdut.jpg"
            message = "Mai exersează! Ai pierdut de data aceasta."

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_id = self.canvas.create_image(self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2, anchor="center", image=self.photo)

        self.text_id = self.canvas.create_text(self.canvas.winfo_width() // 2, self.canvas.winfo_height() - 100, text=f"{message}\nScor: {self.score}/{len(self.questions)}", font=("Arial", 24, "bold"), fill="black", anchor="center")

        # Îndepărtăm butonul de restart existent (dacă există)
        if hasattr(self, 'restart_button'):
            self.restart_button.destroy()

        # Adăugăm butonul de restart
        self.restart_button = tk.Button(self.root, text="Restart joc", font=("Arial", 16), command=self.reset_game)
        self.restart_button.pack(pady=20)

        self.canvas.bind("<Configure>", self.resize_image)

    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        resized_image = self.image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(resized_image)
        self.canvas.itemconfig(self.image_id, image=self.photo)
        self.canvas.coords(self.image_id, new_width // 2, new_height // 2)
        self.canvas.coords(self.text_id, new_width // 2, new_height - 100)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def reset_game(self):
        # Resetăm jocul
        self.current_question = 0
        self.score = 0

        # Reîncărcăm prima întrebare și repopulăm interfața
        self.clear_window()
        self.__init__(self.root)

# Creăm fereastra principală
main_window = tk.Tk()
quiz_app = QuizApp(main_window)

# Pornim aplicația
main_window.mainloop()
"""
import tkinter as tk
from PIL import Image, ImageTk

class QuizApp:
    def __init__(self, main_window):
        self.root = main_window
        self.root.title("Quiz App")
        self.root.geometry( "800x600")

        # Încărcăm imaginea de fundal
        self.background_image = Image.open("Vrei_sa_fii_milionar.png")
        self.background_image = self.background_image.resize((800, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.background_image)

        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        self.thumb_up_img = Image.open("thumbs_up.png")
        self.thumb_up_img = self.thumb_up_img.resize((200, 200), Image.Resampling.LANCZOS)
        self.thumb_up = ImageTk.PhotoImage(self.thumb_up_img)

        self.thumb_down_img = Image.open("thumbs_down.png")
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
                "question": "Care este rezulatul calcului: 5+25:5-3?",
                "options": ["7", "3", "15", "9"],
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

        # Eticheta pentru întrebări
        self.question_label = tk.Label(self.root, text="", font=("Arial", 24, "bold"), wraplength=700, bg="white", fg="black", anchor="center")
        self.question_label.pack(pady=20)

        # Rama pentru butoane
        self.button_frame = tk.Frame(self.root, bg="black")
        self.button_frame.pack()

        # Butoane pentru opțiuni
        self.options_buttons = []
        for i in range(4):
            button = tk.Button(self.button_frame, text="", font=("Arial", 16, "bold"), width=20, height=2, command=lambda i=i: self.check_answer(i))
            self.options_buttons.append(button)

        self.options_buttons[0].grid(row=0, column=0, padx=10, pady=10)
        self.options_buttons[1].grid(row=0, column=1, padx=10, pady=10)
        self.options_buttons[2].grid(row=1, column=0, padx=10, pady=10)
        self.options_buttons[3].grid(row=1, column=1, padx=10, pady=10)

        self.load_question()

        # Label pentru degetul mare
        self.thumb_label = tk.Label(self.root)
        self.thumb_label.pack(pady=20)

        # Buton de reset
        self.reset_button = tk.Button(self.root, text="Resetează jocul", font=("Arial", 16), command=self.reset_game, bd=0, relief="flat", bg="lightblue", fg="black")
        self.reset_button.place(relx=0.5, rely=0.9, anchor="center")

    def load_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])

        for i in range(4):
            self.options_buttons[i].config(text=question_data["options"][i], state="normal", bg="lightblue", fg="black")

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["answer"]

        for btn in self.options_buttons:
            btn.config(bg="lightblue")

        if selected_option == correct_answer:
            self.score += 1
            self.options_buttons[selected_option].config(bg="lightgreen", fg="black")
            self.thumb_label.config(image=self.thumb_up)
        else:
            self.options_buttons[selected_option].config(bg="lightcoral", fg="black")
            correct_option = self.questions[self.current_question]["options"][correct_answer]
            self.options_buttons[correct_answer].config(bg="lightgreen", fg="black")
            self.thumb_label.config(image=self.thumb_down)

        self.root.after(1000, self.clear_thumb_image)
        self.root.after(1000, self.next_question)

    def clear_thumb_image(self):
        self.thumb_label.config(image="")

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        self.clear_window()

        if self.score == len(self.questions):
            image_path = ("trofeu.webp")
            message = "Felicitări! Ești un câștigător!"
        elif self.score >= len(self.questions) // 2:
            image_path = "mai incearca.jpg"
            message = "Mai exersează! Poți face mai bine data viitoare!"
        else:
            image_path = "ai pierdut.jpg"
            message = "Mai exersează! Ai pierdut de data aceasta."

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_id = self.canvas.create_image(self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2, anchor="center", image=self.photo)

        self.text_id = self.canvas.create_text(self.canvas.winfo_width() // 2, self.canvas.winfo_height() - 100, text=f"{message}\nScor: {self.score}/{len(self.questions)}", font=("Arial", 24, "bold"), fill="black", anchor="center")

        # Îndepărtăm butonul de restart existent (dacă există)
        if hasattr(self, 'restart_button'):
            self.restart_button.destroy()

        # Adăugăm butonul de restart centrat
        self.restart_button = tk.Button(self.root, text="Restart joc", font=("Arial", 16), command=self.reset_game, bd=0, relief="flat", bg="lightblue", fg="black")
        self.restart_button.place(relx=0.5, rely=0.9, anchor="center")  # Centrat pe fereastră

        self.canvas.bind("<Configure>", self.resize_image)

    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        resized_image = self.image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(resized_image)
        self.canvas.itemconfig(self.image_id, image=self.photo)
        self.canvas.coords(self.image_id, new_width // 2, new_height // 2)
        self.canvas.coords(self.text_id, new_width // 2, new_height - 100)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def reset_game(self):
        # Resetăm jocul
        self.current_question = 0
        self.score = 0

        # Reîncărcăm prima întrebare și repopulăm interfața
        self.clear_window()
        self.__init__(self.root)

# Creăm fereastra principală
main_window = tk.Tk()
quiz_app = QuizApp(main_window)

# Pornim aplicația
main_window.mainloop()
