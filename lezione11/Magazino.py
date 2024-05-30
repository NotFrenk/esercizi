# Gestione di un magazzino
# Scrivi un programma in Python che gestisca un magazzino. 
# Il programma deve permettere di aggiungere prodotti al magazzino, 
# cercare prodotti per nome e verificare la disponibilità di un prodotto.

# Definisci una classe Prodotto con i seguenti attributi:
# - nome (stringa)
# - quantità (intero)
 
# Definisci una classe Magazzino con i seguenti metodi:
# - aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
# - cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
# - verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
# Test case:

#     Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. 
# Successivamente, aggiunge i prodotti al magazzino.
#     Il sistema cerca un prodotto per verificare se esiste nell'inventario.
#     Il sistema verifica la disponibilità dei prodotti in inventario.


class Prodotto:
    def __init__(self, nome:str, quantità:int):
        self.nome = nome
        self.quantità = quantità 

class Magazzino:
    def __init__(self):
        self.inventario = []

    def aggiungi_prodotto(self, prodotto: Prodotto):
        self.inventario.append(prodotto)

    def cerca_prodotto(self, nome: str) -> Prodotto:
        for prodotto in self.inventario:
            if prodotto.nome == nome:
                return prodotto
        return None
    
    def verifica_disponibilità(self, nome: str) -> str:
        prodotto = self.cerca_prodotto(nome)
        if prodotto:
            return f"Il prodotto {nome} è disponibile in quantità: {prodotto.quantità}."
        else:
            return "Il prodotto non è disponibile in magazzino"




magazzino = Magazzino()

# Aggiungi prodotti al magazzino
prodotto1 = Prodotto("Lampada", 50)
prodotto2 = Prodotto("Sedia", 100)
prodotto3 = Prodotto("Tavolo", 30)

magazzino.aggiungi_prodotto(prodotto1)
magazzino.aggiungi_prodotto(prodotto2)
magazzino.aggiungi_prodotto(prodotto3)


# Cerca un prodotto per nome
print(magazzino.cerca_prodotto("Sedia"))  
# Output: <__main__.Prodotto object at 0x7f7f05304be0>

# Verifica disponibilità di un prodotto
print(magazzino.verifica_disponibilità("Tavolo"))  
# Output: Il prodotto Tavolo è disponibile in quantità: 30.
print(magazzino.verifica_disponibilità("Computer"))  
# Output: Il prodotto non è disponibile in magazzino.