"Quiz App" este o aplicație educativă interactivă dezvoltată în Python, utilizând biblioteca Tkinter pentru interfața grafică și Pillow pentru manipularea imaginilor. Scopul aplicației este de a oferi utilizatorilor o experiență plăcută și captivantă, ajutându-i să învățe și să testeze cunoștințele în diverse domenii. Prin feedback vizual imediat, utilizatorii pot identifica rapid răspunsurile corecte și greșelile, ceea ce contribuie la procesul de învățare.

Aplicația oferă suport pentru imagini personalizate și include funcții de punctaj, evaluare finală și resetare. Fiecare sesiune este compusă dintr-un set de întrebări cu patru opțiuni multiple, iar la final, utilizatorul primește un mesaj motivațional și un scor.

#### Caracteristici Detaliate
1. **Interfață grafică atractivă**:
   - Fundal personalizat cu o imagine tematică.
   - Butoane și elemente pentru interfață cu utilizatorul proiectate pentru a fi clare și accesibile.
   - Utilizarea imaginilor sugestive (degete mari în sus/jos) pentru feedback instantaneu la fiecare întrebare.

2. **Sistem de quiz**:
   - Oferă o serie de întrebări, fiecare având patru opțiuni de răspuns.
   - Feedback instant pentru răspunsurile corecte și greșite prin schimbarea culorii butoanelor și afișarea imaginilor relevante.

3. **Punctaj și evaluare finală**:
   - Calculul scorului pe baza răspunsurilor corecte.
   - Mesaj personalizat și afișarea unei imagini relevante în funcție de performanță (trofeu pentru scor perfect, mesaj motivațional pentru scor mediu, și imagine de consolare pentru scor mic).

4. **Flexibilitate**:
   - Posibilitatea de a reseta jocul și de a reîncepe quiz-ul de la întrebarea inițială.

5. **Compatibilitate**:
   - Aplicația funcționează pe orice sistem de operare care suportă Python și bibliotecile utilizate.

#### Biblioteci Utilizate
1. **Tkinter**:
   - Biblioteca standard pentru crearea de interfețe grafice în Python.
   - Elemente utilizate: `Label`, `Button`, `Frame`, `Canvas`, `MessageBox`.

2. **Pillow (PIL)**:
   - Biblioteca folosită pentru manipularea imaginilor.
   - Funcții utilizate: redimensionare, încărcare imagini, conversii.


#### Fișiere Necesare
1. **Imagini**:
   - `Vrei_să_fii_milionar.png`: Imaginea de fundal.
   - `thumbs_up.png`: Imagine utilizată pentru feedback la răspunsuri corecte.
   - `thumbs_down.png`: Imagine utilizată pentru feedback la răspunsuri greșite.
   - `trofeu.webp`: Imagine utilizată pentru scor perfect.
   - `mai incearca.jpg`: Imagine pentru scor mediu.
   - `ai pierdut 1.webp`: Imagine utilizată pentru scor mic.

2. **Fișier Python**:
   - Scriptul principal al aplicației (`quiz_app.py`).

Asigură-te că toate fișierele necesare sunt în același director cu scriptul pentru a evita erorile legate de calea fișierelor.



#### Cum Funcționează Aplicația
1. **Încărcarea unei întrebări**:
   - Fiecare întrebare este extrasă dintr-o listă predefinită de întrebări.
   - Opțiunile sunt asociate butoanelor din interfață.

2. **Feedback imediat**:
   - Utilizatorul primește feedback vizual imediat după selectarea unei opțiuni (verde pentru corect, roșu pentru greșit).
   - Imaginile de feedback (thumbs up/thumbs down) sunt afișate temporar.

3. **Calcularea scorului**:
   - Fiecare răspuns corect adaugă un punct la scorul utilizatorului.

4. **Evaluare finală**:
   - La terminarea setului de întrebări, utilizatorul primește o evaluare sub formă de text și imagini relevante.

5. **Resetare joc**:
   - Aplicația revine la starea inițială, permițând utilizatorului să joace din nou.



