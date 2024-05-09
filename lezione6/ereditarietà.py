from typing import Tuple

class Persona:
    def __init__(self, nome:str, cognome:str, data_di_nascita:str, genere:str) -> None:

        self.nome: str = nome
        self.cognome:str = cognome
        self.data_di_nascita:str = data_di_nascita
        self.genere:str = genere

    def calcola_età(self)->int:

        return 10



persona_1:Persona = Persona(nome="Flavio",
                            cognome="Giorgi",
                            data_di_nascita="24/12/94",
                            genere="Maschio")


class Dipendente(Persona):

    def __init__(self, nome: str, 
                 cognome: str, 
                 data_di_nascita: str, 
                 genere: str) -> None:
        super().__init__(nome, cognome, data_di_nascita, genere)
    
    def calcola_stipendio(self):
        return 500.0


dipendente_1:Dipendente = Dipendente(nome="Flavio",
                            cognome="Giorgi",
                            data_di_nascita="24/12/94",
                            genere="Maschio")

print(persona_1.calcola_età())
#print(persona_1.calcola_stipendio()) da errore perche la callse 'persona' non ha la funzione           

print(dipendente_1.nome)
print(dipendente_1.calcola_età())
print(dipendente_1.calcola_stipendio())