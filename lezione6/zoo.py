class Zoo:
    def __init__(self):
        self.fences:list[Fence] = []
        self.zoo_keepers:list[ZooKeeper] = []




class Animal:
    def __init__ (self, name:str, species:str, age:int, height:float, width:float, preferred_habitat:str):
        self.name:str = name
        self.species:str = species
        self.age:int = age
        self.height:float = height
        self.width:float = width
        self.preferred_habitat :str =preferred_habitat
        self.health:float=round(100 * (1 / age), 3)

    def __str__(self):
        return f'Animal(name={self.name}, species={self.species}, age={self.age}, health={self.health})'

class Fence:
    def __init__(self, area:float, temperature:float, habitat:str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []

    def __str__(self):
        return f'Fence(area={self.area}, temperature={self.temperature}, habitat={self.habitat})'



class ZooKeeper:
    def __init__(self, name:str, surname:str, id:str):
        self.name:str=name
        self.surname:str = surname
        self.id:str = id

    def add_animal(self, animal: Animal, fence: Fence, zoo):
        if fence.area >= animal.height * animal.width and fence.habitat == animal.preferred_habitat:
                fence.area -= animal.height * animal.width
                fence.animals.append(animal)
                print(f'{animal.name} aggiunto in {fence}')
        else:
            print(f'{animal.name} non può essere inserito in {fence}')
        
    def remove_animal(self, animal:Animal, fence:Fence, zoo):
        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.area += animal.height * animal.width
            print(f'{animal.name} è stato rimosso')

    def feed(self, animal: Animal, fence: Fence, ):
        for fence in zoo.fences:
            for animal in fence.animals:
                if animal.health < 100 and fence.area >= animal.height * animal.width * 1.02:
                    animal.health += 1
                    animal.height *= 1.02
                    animal.width *= 1.02
                    fence.area -= animal.height * animal.width
                    print(f"{animal.name} è stato nutrito.")

    def clean(fence: Fence) -> float:
        


    def __str__(self):
        return f"ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})"





if __name__ == "__main__":
    #creating a zoo istance
    zoo = Zoo()
     #creating a zookeper istance and adding it to the zoo
    zoo_keeper = ZooKeeper("Lorenzo", "Maggi", 1234)
    zoo.zoo_keepers.append(zoo_keeper)
   # creating a fence istanche and ad it to the zoo
    fence = Fence(area=100, temperature=25, habitat="Continentale")
    zoo.fences.append(fence)
    #creating animal istances
    animal1 = Animal(name="Scoiattolo", species="Blabla", age=25, height=5, width=2, preferred_habitat="Continentale")
    animal2 = Animal(name="Lupo", species="Lupus", age=14, height=8, width=3, preferred_habitat="Continentale")
    #add and remove animal tries
    zoo_keeper.add_animal(animal1, fence, zoo)
    zoo_keeper.add_animal(animal2, fence, zoo)
    zoo_keeper.remove_animal(animal1, fence, zoo)

    zoo_keeper.feed(animal1, fence)

    zoo.describe_zoo()