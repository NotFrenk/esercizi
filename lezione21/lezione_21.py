# def generatore():
#     yield "A"
#     yield 'B'
#     yield 'C'

# prova_generatore = generatore()

# print(next(prova_generatore))
# print(next(prova_generatore))
# print(next(prova_generatore))
# print(next(prova_generatore))

 


import time 
# from contextlib import contextmanager

# @contextmanager
# def contex_manager_decorator():

#     start_time = time.time()

#     yield

#     end_tieme = time.time()
#     elapsed_time = end_tieme - start_time

#     print(f'{elapsed_time=}')

# @contex_manager_decorator
# def area_cerchio(raggio: float):

#     return raggio * raggio * 3.14

# area_cerchio(1)

import sys


a =[]
b=a
print(sys.getrefcount(a))