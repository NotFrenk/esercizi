
# def ciao(name:str):
#     return f'ciao, {name}'

# def saluta(func):
#     return func('bob')

# def salve(name:str):
#     return f'salve, {name}'

# print(saluta(ciao))
# print(saluta(salve))


# def parent():
#     print(f'sono in parent')

#     def first_child():
#         print(f'sono in First child')

#     def second_chilld():
#         print(f'sono in second child')

#     second_chilld()
#     second_chilld()
#     first_child()

# parent()

def parent():
    print(f'sono in parent')

    def first_child():
        print(f'sono in First child')
        
    return first_child


print(parent())