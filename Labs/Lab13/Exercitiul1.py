import os

def rename_files_in_folder(folder_path):
    """
    Redenumește fișierele dintr-un folder specificat, adăugând prefixul 'renamed_'.

    Args:
        folder_path (str): Calea către folderul care conține fișierele de redenumit.
    """
    try:
        # Verificăm dacă folderul există
        if not os.path.exists(folder_path):
            print(f"Folderul specificat nu există: {folder_path}")
            return

        # Obținem lista de fișiere din folder
        files = os.listdir(folder_path)

        if not files:
            print(f"Folderul '{folder_path}' este gol.")
            return

        # Iterăm prin fișiere și le redenumim
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)

            # Verificăm dacă este fișier, nu director
            if os.path.isfile(file_path):
                new_name = f"renamed_{file_name}"
                new_path = os.path.join(folder_path, new_name)
                os.rename(file_path, new_path)
                print(f"{file_name} -> {new_name}")

        print("Redenumirea fișierelor s-a finalizat.")

    except Exception as e:
        print(f"A apărut o eroare: {e}")

if __name__ == "__main__":
    # Solicităm utilizatorului calea către folder
    folder = input("Introduceți calea către folderul cu fișierele de redenumit: ").strip()
    rename_files_in_folder(folder)
