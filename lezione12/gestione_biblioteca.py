# Sistema di Gestione Biblioteca
# Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. 
# Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione 
# degli stessi. 
# Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli
# e visualizzare quali libri sono disponibili in un dato momento.
 
# Classi:
# - Libro: Rappresenta un libro con titolo, autore, stato del prestito. 
# Il libro deve essere inizialmente disponibile (non prestato).

# - Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

#     Metodi:
#     - aggiungi_libro(libro): 
#       Aggiunge un nuovo libro al catalogo della biblioteca. 
#       Restituisce un messaggio di conferma.

#     - presta_libro(titolo): 
#       Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. 
#       Restituisce un messaggio di stato.

#     - restituisci_libro(titolo): 
#       Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile.        
#       Restituisce un messaggio di stato.

#     - mostra_libri_disponibili(): 
#       Restituisce una lista dei titoli dei libri attualmente disponibili. 
#       Se non ci sono libri disponibili, restituisce un messaggio di errore.

# Test Cases:
# - Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
# - Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
# - L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
# - In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.

class Libro:

    def __init__(self, titolo:str, autore:str):
        self.titolo=titolo
        self.autore=autore
        self.disponibile=True

    def __str__(self):
        return f"'{self.titolo}' di {self.autore} - {'Disponibile' if self.disponibile else 'Non disponibile'}"

    
class Biblioteca:

    def __init__(self):
        self.catalogo:list=[]

    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)
        return f'{libro.titolo} aggiunto nel catalogo'
    
    def presta_libro(self, titolo:str):
        for libro in self.catalogo:
            if libro.titolo==titolo:
                if libro.disponibile:
                    libro.disponibile = False
                    return f'{titolo} è stato prestato'
                else:
                    return f'{titolo} è già stato prestato'
        return f'nessun libro trovato con titolo: {titolo}'

    def restituisci_libro (self, titolo:str):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if not libro.disponibile:
                    libro.disponibile = True
                    return f'libro {titolo} restituito con successo'
                else:
                    return f'libro {titolo} è già disponibile'
        return f'nessun libro trovato con titolo: {titolo}'

    def mostra_libri_disponibili (self):
        libri_disponibili:list =[libro.titolo for libro in self.catalogo if libro.disponibile]
        if libri_disponibili:
            return libri_disponibili
        else:
            return f'Nessun libro è disponibile al momento'


if __name__ == "__main__":
    # Creazione di alcuni libri
    libro1 = Libro("Il Nome della Rosa", "Umberto Eco")
    libro2 = Libro("1984", "George Orwell")
    libro3 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien")

    # Creazione della biblioteca
    biblioteca = Biblioteca()

    # Aggiunta dei libri al catalogo
    print(biblioteca.aggiungi_libro(libro1))
    print(biblioteca.aggiungi_libro(libro2))
    print(biblioteca.aggiungi_libro(libro3))

    # Prestito di un libro
    print(biblioteca.presta_libro("1984"))

    # Tentativo di prestare un libro già prestato
    print(biblioteca.presta_libro("1984"))

    # Restituzione di un libro
    print(biblioteca.restituisci_libro("1984"))

    # Tentativo di restituire un libro già disponibile
    print(biblioteca.restituisci_libro("1984"))

    # Visualizzazione dei libri disponibili
    print("Libri disponibili:")
    print(biblioteca.mostra_libri_disponibili())