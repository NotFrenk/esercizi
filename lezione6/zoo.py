class Zoo:
    def __init__(self, fences=None, zoo_keepers=None):
        self.fences = []
        self.zoo_keepers = []
    
    def add_fence(self, fence):
        self.fences.append(fence)
    
    def add_zoo_keeper(self, zoo_keeper):
        self.zoo_keepers.append(zoo_keeper)




class Animal:
    def __init__ (self, name:str, species:str, age:int, height:float, width:float, preferred_habitat:str, health:float):

        self.name:str = name
        self.species:str = species
        self.age:int = age
        self.height:float = height
        self.width:float = width
        self.preferred_habitat :str =preferred_habitat
        self.health:float = health

        healt:float=round(100 * (1 / age), 3)


class Fence:
    def __init__(self, area:float, temperature:float, habitat:str):
        if animals is None:
            animals = []
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = animals

    def add_animal(self, animal):
        self.animals.append(animal)

class ZooKeeper(Fence):
    def __init__(self, name:str, surname:str, id:str, area: float, temperature: float, habitat: str):
        super().__init__(area, temperature, habitat)
        self.name:str=name
        self.surname:str = surname
        self.id:str = id

    def add_animal(animal: Animal, fence: Fence):
        if fence.area >= animal.height * animal.width:
             if fence.habitat == animal.preferred_habitat:
                fence.add_animal(animal)
        
    def remove_animal(self, animal, fence):
        if animal in fence.animals:
            fence.remove_animal(animal)
            fence.restore_area(animal)
            

        
            

            
            












