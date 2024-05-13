class Animale:
    def __init__(self,nome:str, specie:str, età:int):
        self.specie=specie
        self.età=età
        self.nome=nome



class Persona(Animale):
    def __init__(self, nome: str, cognome:str, età: int, cf:str):
        super().__init__(nome, 'homo sapiens', età)
        self.cognome=cognome
        self.età=età
        self.cf=cf

    def __str__(self) -> str:
        return f'{self.nome.capitalize()} {self.cognome.capitalize()}(cf={self.cf})'



class Studente(Persona):
    def __init__(self, nome: str, età: int, cf: str, matricola:int):
        super().__init__(nome, età, cf)
        self.matricola=matricola


    


class gatto(Animale):
    def __init__(self, nome: str, specie: str, età: int):
        super().__init__(nome, 'felidea', età)



class coniglio(Animale):
    def __init__(self, nome: str, specie: str, età: int):
        super().__init__(nome, specie, età)


persona1 = Persona(nome='Lorenzo', cognome='maggi', cf='ciao' ,età=22)
print(persona1)

gatto1= gatto(name='bombo',età=3)
print(gatto1)