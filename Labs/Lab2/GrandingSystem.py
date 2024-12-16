def grading_system(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif  70 <= score < 80:
        return "C"
    elif 60 <= score <70:
        return "D"
    elif 0 <= score < 60:
        return "F"
    else:
       return "Punctaj invalid"
try:
    score = int(input("Introdu un scor între 0 și 100:"))
    print("Nota", grading_system(score))
except ValueError:
    print("Te rog introdu un număr valid!")

