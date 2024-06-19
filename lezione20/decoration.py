def decoraton(func):

    def wrapper():
        print(f'Prima di func')

        func()

        print(f'Dopo func')

    return wrapper

def ciao():
    print ('ciao')

ciao = decoraton(ciao)

ciao()




def decoraton(func):

    def wrapper():
        import time

        start = time.time()

        func()

        print(f'time elapsed: {time.time()}')

    return wrapper

def ciao():
    print ('ciao')

ciao = decoraton(ciao)

ciao()
