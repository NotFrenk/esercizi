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

"""

"""

animale1=Animal("giraffa", "giraffonica", 5, 7.5, 3, "savana", 50)



class Fence:
    def __init__(self, area:float, temperature:float, habitat:str):
        self.area:float = area
        self.temperature:float = temperature
        self.habitat:str = habitat


class ZooKeeper:
    def __init__(self, name:str, surname:str, id:str,):
        self.name:str=name
        self.surname:str = surname
        self.id:str = id

    def add_animal(animal: Animal, fence: Fence):
        if animal.height and animal.width <= fence.area:
            print("entgra")


animale1.




class Zoo:
    def __init__(self, fences:list[Fence], zoo_keepers:list[ZooKeeper]):
        self.fences:list[Fence] = fences
        self.zoo_keepers:list[ZooKeeper] = zoo_keepers






