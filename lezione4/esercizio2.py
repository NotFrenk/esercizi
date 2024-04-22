"""
data una stringa s che contiene parole e spazzi,
restituie la lunghezza dell'ultima parola in s.

Una parola è una sottostringa che contine caratteri contigui deversi dallo spazio

Esempio 1
s= "hello world" -> restituire 5
l'ultima parola è "world" ch ha lunghezza 5

Esempio2
s="    fly me    to    the  moon   " -> restituire 4
l'ultima parola è "moon" che ha lunghezza 4

"""

def lengt_of_last_word(s:str) -> int:
    
    s:str=s.strip()
    l:list[str] = s.split()
    return len(1[-1])    

    