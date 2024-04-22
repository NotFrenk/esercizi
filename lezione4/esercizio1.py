"""
dato un intero x, restituisce true se x è palindromo, e falso se altrimenti

Esempio 1
x=121 -> true
spiegazione: 121 si legge come 211 sia da destra che da sinistra

Esempio 2
x= -121 -> fase
spiegazione: da sinistra a destra, leggiamo -121. da destra a snisra, abbiamo 121-
             percio,questo numero non è palindromo 

Esempio 3:
x = 10 -> false
spiegazione: 01 da destra a sinistra perciò non è palindromo 
"""

"""
def is_palindrome(x:int) -> bool:
    s:str = str(x)
    s1 = reversed(s)
    return s==s1
"""    

def is_palindrome(x:int) -> bool:
    s:str=str(x)
    i:str=0
    while i < len(s): #for i in range(len(s))
        j=len(s)-(i+1)
        if s[i] !=s[j]:
            return False
        i += 1
    return True