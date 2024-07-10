from multiprocessing import Process
import time

def bubble_sort_v2(x: list[int]):
    # Ω(n) -> caso migliore quando la lista è già ordinata
    # O(n^2) -> caso peggiore
    from random import randint

    x= [randint(0, 10000) for _ in range(10000)]

    ho_fatto_swap: bool = True
    for i in range(len(x)):
        for j in range(len(x) - i - 1):
            if x[j] > x[j+1]:
                # swap(x[j], x[j+1])
                ho_fatto_swap = False
                temp: int = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
        if ho_fatto_swap:
            break

def sleep():

    print (f'sono nella funzione')

    time.sleep(60)

    print (f'sto uscendo dalla funzione')

if __name__ == '__main__':
    tic: float = time.time()

    t1= Process(target=sleep)
    t2=Process(target=sleep)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    toc: float = time.time()
    time_elapsed: float = toc - tic

    print(f'{time_elapsed=}')