l = lambda v, f, t: v if f == t else {('C','F'):lambda c:c*9/5+32, ('C','K'):lambda c:c+273.15, ('F','C'):lambda f:(f-32)*5/9, ('F','K'):lambda f:(f-32)*5/9+273.15, ('K','C'):lambda k:k-273.15, ('K','F'):lambda k:(k-273.15)*9/5+32}[(f, t)](v)
valoare = float(input("Valoare: "))
print(round(l(valoare, input("Din: ").strip().upper(), input("In: ").strip().upper()), 2))
