# RENDERING GRAFICO
# Si vuole sviluppare un sistema in Python per gestire il rendering di diverse forme geometriche. 
# Il sistema dovrà supportare almeno tre tipi di forme: quadrati, rettangoli, e triangoli rettangoli.

# Definire la classe astratta Forma che sarà utilizzata per definire l'attributo corrispondente al nome della forma e le funzionalità base di ogni forma, 
# come i metodi astratti getArea() per calcolare l'area e render() per disegnare su schermo la forma.

from abc import (ABC) 

class Forma(ABC):
    def __init__(self, nome):
        self.nome=nome

    def getArea(self):
        pass

    def render(self):
        pass

# Definire la classe Quadrato che estende la classe Forma e aggiunge specifiche circa la lunghezza di un suo lato.
# Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare il nome della forma su "Quadrato".
# Il metodo getArea() deve calcolare l'area del quadrato.
# Il metodo render() deve stamapre su schermo un quadrato avente lato pari al valore passato nel costruttore. 
# Il quadrato da stampare deve essere un quadrato vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)
 
class Quadrato(Forma):
    def __init__(self, lunghezza_lato):
        super().__init__("Quadrato")
        self.lunghezza_lato=lunghezza_lato

    def getArea(self):
        return self.lunghezza_lato * self.lunghezza_lato
    
    def render(self):
        print(f'Ecco un {self.nome} di lato {self.lunghezza_lato}')
        for i in range(self.lunghezza_lato):
            for j in range(self.lunghezza_lato):
                if i == 0 or i == self.lunghezza_lato -1 or j == 0 or j == self.lunghezza_lato -1:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
        print (f'L\'area di questo {self.nome} vale: {self.getArea()}')

# Definire la classe Rettangolo che estende la classe Forma e aggiunge specifiche circa la lunghezza della sua base e della sua altezza.
# Il costruttore della classe deve ricevere come argomento solo la base e l'altezza del rettangolo, ed impostare il nome della forma su "Rettangolo".
# Il metodo getArea() deve calcolare l'area del rettangolo.
# Il metodo render() deve stampare su schermo un rettangolo avente base ed altezza pari ai valori passati nel costruttore. 
# Il rettangolo da stampare deve essere un rettangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

class Rettangolo(Forma):
    def __init__ (self, base, altezza):
        super().__init__('Rettangolo')
        self.base=base
        self.altezza=altezza 
    
    def getArea(self):
        return self.base * self.altezza
    
    def render(self):
        print(f'Ecco un {self.nome} avente base {self.base} ed altezza {self.altezza}!')
        for r in range(self.base):
            for c in range(self.altezza):
                if r == 0 or r == self.base -1 or c == 0 or c == self.altezza -1:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
        print(f'L\'area di questo {self.nome} vale: {self.getArea()}')


# Definire la classe Triangolo che estende la classe Forma e aggiunge specifiche circa la dimensione di un lato del triangolo 
# (per semplicità, si suppone che il triangolo in questione sia un triangolo rettangolo).
# Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, ed impostare il nome della forma su "Triangolo".
# Il metodo getArea() deve calcolare l'area del triangolo.
# Il metodo render() deve stampare su schermo un triangolo rettangolo avente i due cateti di lunghezza pari ai valori passati nel costruttore. 
# Il triangolo da stampare deve essere un triangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

class Triangolo(Forma):
    def __init__(self, lato):
        super().__init__('Triangolo')
        self.lato = lato

    def getArea(self):
        return self.lato * self.lato // 2
    
    def render(self):
        print(f'Ecco un {self.nome} avente base {self.lato} ed altezza {self.lato}!')
        for r in range(self.lato):
            for c in range(self.lato):
                if c == 0 or r == self.lato - 1 or r == c:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
        print(f'L\'area di questo {self.nome} vale: {self.getArea()}')

# Hint: per il disegno utilizzare print("*", end=" "), dato che l'argomento end = " " permette di controllare come termina ogni chiamata a print,
# e impostandolo a uno spazio si può fare in modo che tutte le stampe successive siano sulla stessa riga, separate da uno spazio.

# Esempi di output:
# Ecco un Quadrato di lato 4!

# * * * *
# *     *
# *     *
# * * * *
# L'area di questo quadrato vale: 16

# Ecco un Rettangolo avente base 8 ed altezza 4!
# * * * * * * * *
# *             *
# *             *
# * * * * * * * *
# L'area di questo rettangolo vale: 32

# Ecco un Triangolo avente base 4 ed altezza 4!
# *      
# * *    
# *   *  
# * * * *
# L'area di questo triangolo vale: 8.0







# Esempi di utilizzo:
quadrato = Quadrato(4)
quadrato.render()

rettangolo = Rettangolo(4,6)
rettangolo.render()

triangolo = Triangolo(5)
triangolo.render()