# Sistema di Prenotazione Cinema

# Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. 
# Il cinema ha diverse sale, ognuna con un diverso film in programmazione. 
# Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
# Classi:
# - Film: Rappresenta un film con titolo e durata.
 
# - Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

# Metodi:
#     - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. 
# Restituisce un messaggio di conferma o di errore.
#     - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
# - Cinema: Gestisce le operazioni legate alla gestione delle sale.

# Metodi:
#     - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
#     - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. 
# Restituisce un messaggio di stato.

# Test case:

#     Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
#     Un cliente sceglie un film e prenota un certo numero di posti.
#     Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.


class Film:
    def __init__(self, titolo:str, durata:int) -> None:
        self.titolo:str=titolo
        self.durata:int=round(durata)


class Sala:
    def __init__(self, id:int, film:str, posti_totali:int, ) -> None:
        self.id=id
        self.film=film
        self.posti_totali= posti_totali
        self.posti_prenotati=0
        
    def prenota_posti(self, num_posti):
        posti_disponibili = self.posti_totali - self.posti_prenotati
        if num_posti <= posti_disponibili:
            self.posti_prenotati += num_posti
            return (f'Prenotazione confermata per {num_posti} per il film: {self.film.titolo}'\
                    f'\nposti ancora disponibili: {posti_disponibili - num_posti}')
        else:
            return (f'Posti non disponibili')
        
    def posti_disponibili(self):
        return self.posti_totali - self.posti_prenotati
    

class Cinema:
    def __init__(self) -> None:
        self.sale= []

    def aggiungi_sala(self, sala):
        self.sale.append(sala)

    def prenota_film (self, titolo_film, num_posti):
        for sala in self.sale:
            if sala.film.titolo == titolo_film:
                return sala.prenota_posti(num_posti)
        return 'film non trovato'
    

cinema = Cinema()

# Aggiungi sale
sala1 = Sala(1, Film("Interstellar", 150), 100)
sala2 = Sala(2, Film("Inception", 140), 80)
cinema.aggiungi_sala(sala1)
cinema.aggiungi_sala(sala2)

# Prenota posti
print(cinema.prenota_film("Interstellar", 3))  # Prenotazione confermata per 3 posti per il film Interstellar.
print(cinema.prenota_film("Inception", 90))    # Posti non disponibili per questa prenotazione.
print(cinema.prenota_film("Tenet", 2))         # Film non trovato.



