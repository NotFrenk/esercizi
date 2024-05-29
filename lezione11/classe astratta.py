from abc import ABC, abstractmethod

class AbcAnimal(ABC):


    @abstractmethod
    def verso():

        pass

    @abstractmethod
    def movimento(self):

        pass


class Gatto(AbcAnimal):
    def __init__(self, nome:str) -> None:
        super().__init__()

        self.nome = nome
        self.velocità:float = 10.0 #m/s

    def verso (self):
        return print('Miao!')
    
    def movimento(self, t:int):
        print (self.velocità * t)
    

class Cane(AbcAnimal):
    def __init__(self, nome:str) -> None:
        super().__init__()

        self.nome= nome
        self.velocità:float = 5.0 #m/s

    def verso (self):
        return print('Bau!')
    
    def movimento(self, t:int):
        print (self.velocità * t)
    
    
    
    
mio_gatto: Gatto = Gatto(nome='bombo')
mio_gatto.verso()
mio_gatto.movimento(t=10)
mio_cane: Cane =Cane (nome='pippi')
mio_cane.verso()
mio_cane.movimento(t=10)
