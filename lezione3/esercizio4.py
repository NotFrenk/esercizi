def check_each(l):
    for n in l:
        if n < 5:
            print("minore")
        elif n > 5:
            print("maggiore")
        else:
            print("uguale")

check_each([2, 5, 0.2, 9, 3, 30, 1])