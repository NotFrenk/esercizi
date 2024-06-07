# Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) 
# e una classe derivata Film che rappresenti specificamente un film.
# Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

# Specifiche della Classe Media:
 
# Attributi:
# - title (stringa): Il titolo del media.
# - reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5.

# Metodi:
# - set_title(self, title): Imposta il titolo del media.
# - get_title(self): Restituisce il titolo del media.
# - aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
# - getMedia(self): Calcola e restituisce la media delle valutazioni.
# - getRate(self): Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioni.
# - ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
# - recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, 
# il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
# Titolo del Film: The Shawshank Redemption
# Voto Medio: 3.80
# Giudizio: Bello
# Terribile: 10.00%
# Brutto: 10.00%
# Normale: 10.00%
# Bello: 30.00%
# Grandioso: 40.00%

# Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, 
# aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().

class Media:

    def __init__(self, title:str=''):
        self.title=title
        self.reviews=[]

    def set_title(self,title:str):
        self.title=title

    def get_title(self):
        return self.title
    
    def aggiungiValutazione(self, voto):
        if 1 <= voto <= 5:
            self.reviews.append(voto)
        else:
            print(f"Voto {voto} non valido. Inserire un valore tra 1 e 5.")

    def getMedia(self):
        if not self.reviews:
            return 0
        else:
            return sum(self.reviews) / len(self.reviews)
        
    def getRate(self):
        media=self.getMedia()
        if media < 1.5:
            return 'Terribile'
        elif media < 2.5:
            return 'Brutto'
        elif media < 3.5:
            return 'Normale'
        elif media < 4.5:
            return 'Bello'
        else:
            return 'Grandioso'
        
    def ratePercentage(self, voto):
        if not self.reviews:
            return 0.0
        else:
            return (self.reviews.count(voto) / len(self.reviews)) * 100
        
    def recensione(self):
        print(f'Titolo del film: {self.get_title()}')
        print(f'Voto medio: {self.getMedia():.2f}')
        print(f'Gudizio: {self.getRate()}')
        for voto in range(1,6):
            percentuale = self.ratePercentage(voto)
            descrizione = ['Terribile', 'Brutto', 'Normale', 'Bello', 'Grandioso'][voto-1]
            print(f'{descrizione} : {percentuale:.2f}%')


class Film(Media):
    pass

# Creazione degli oggetti di tipo Film
film1 = Film("The Shawshank Redemption")
film2 = Film("The Godfather")

# Aggiunta delle valutazioni
valutazioni_film1 = [5, 4, 5, 3, 4, 5, 5, 4, 3, 5]
valutazioni_film2 = [5, 5, 5, 4, 4, 3, 4, 4, 5, 5]

for voto in valutazioni_film1:
    film1.aggiungiValutazione(voto)

for voto in valutazioni_film2:
    film2.aggiungiValutazione(voto)

# Visualizzazione delle recensioni
film1.recensione()
print()
film2.recensione()