def check_each(l:list):
    for n in l:
        if len(n)<5:
            print(f"{n} è piu piccolo di 5")
        elif len(n)>5:
            print(f"{n} è piu grande di 5")
        else:
            print(f"{n} è lunga uguale a 5")