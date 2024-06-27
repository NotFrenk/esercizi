def decoraton(func):

    def wrapper():
        print(f'Prima di func')

        func()

        print(f'Dopo func')

    return wrapper

def ciao():
    print ('hey')

ciao = decoraton(ciao)

ciao()






def decorator_time(func):

     def wrapper(*args):
         import time

         start = time.time()

         func(*args)

         print(f'time elapsed: {time.time() - start}')

     return wrapper




def ciao():
    print ('ciao')

ciao = decoraton(ciao)

ciao()

