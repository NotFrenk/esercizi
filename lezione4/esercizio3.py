"""
Dato un intero col_number, restituire il suo corrispondene 
titolo di colonna come ad esempio compare su un foglio excel

Esempio 1:
col_number = 1 -> "A"
col_number = 2 -> "b"
col_number = 26 -> "Z"

Esempio 2
col_number = 27 -> "AA"
col_number = 28 ->"AB"

Esempio 3
col_number = 701 -> "ZY"
"""
def convert_to_title(col_number:int) -> str:
    result:str=""
    while col_number > 0:
        resto= (col_number -1) %26 # mi da il resto
        result = chr(resto + ord('A')) + result
        col_number =(col_number -1) // 26
    return result

"""
col_number=700
result =""
interazione1
 resto=23
 result=
"""