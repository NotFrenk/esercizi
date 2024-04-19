def check_length(parola):
    if len(parola)<10:
        print(f"la parola {parola} è piu corda di 10 caratteri")
    elif len(parola)>10:
        print(f"la paarola {parola} è piu lunga di 10 caratteri")
    else:
        print(f"la parola {parola} è lunga esattamente 10 caratteri")

res=check_length("aereoplano")