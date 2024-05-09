from typing import Tuple

class Persona:
    
    def __init__(self, 
                 name: str, 
                 cognome: str, 
                 data_di_nascita: str,
                 genere: str) -> None:
        
        self.nome: str = name
        self.cognome: str = cognome
        self.data_di_nascita: str = data_di_nascita
        self.genere: str = genere
        
    def calcola_eta(self)->int:
        
        return 10
    
    
    
persona_1: Persona = Persona(name="Flavio", 
                             cognome="Giorgi", 
                             data_di_nascita="24/12/94", 
                             genere="Maschio")


class Dipendente(Persona):
    
    def __init__(self, 
                 name: str, 
                 cognome: str, 
                 data_di_nascita: str, 
                 genere: str,
                 ore_lavorate: int) -> None:
        super().__init__(name, cognome, data_di_nascita, genere)
        self.ore_lavorate: int = ore_lavorate

        
    def calcola_stipendio(self)->float:
        
        return 500.0

    def __str__(self) -> str:
        return super().__str__()


dipendente_1: Dipendente = Dipendente(name="Flavio", 
                             cognome="Giorgi", 
                             data_di_nascita="24/12/94", 
                             genere="Maschio",
                             ore_lavorate=500)



class Professore(Dipendente):
    
    def __init__(self, 
                 name: str, 
                 cognome: str, 
                 data_di_nascita: str, 
                 genere: str, 
                 ore_lavorate: int,
                 materia_insegnata: str,
                 ore_di_lezione: int) -> None:
        super().__init__(name, cognome, data_di_nascita, genere, ore_lavorate)
        
        self.materia_insegnata: str = materia_insegnata
        self.ore_di_lezione: int = ore_di_lezione
        
    def __str__(self) -> str:
        return super().__str__()

print(persona_1.calcola_eta())

print(dipendente_1.ore_lavorate)
print(dipendente_1.nome)
print(dipendente_1.calcola_eta())
print(dipendente_1.calcola_stipendio())



professore_1: Professore = Professore(name="Flavio", 
                             cognome="Giorgi", 
                             data_di_nascita="24/12/94", 
                             genere="Maschio",
                             ore_lavorate=500,
                             materia_insegnata="Python",
                             ore_di_lezione=1000)

print(professore_1.ore_di_lezione)
