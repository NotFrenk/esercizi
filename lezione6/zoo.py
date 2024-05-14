



class Animal:
    def __init__ (self, name:str, species:str, age:int, height:float, width:float, preferred_habitat:str):
        self.name:str = name
        self.species:str = species
        self.age:int = age
        self.height:float = height
        self.width:float = width
        self.preferred_habitat :str =preferred_habitat
        self.health:float=round(100 * (1 / age), 3)

        if age <= 0:
            age=1
        elif height <=0:
            height=3
        elif width <=0:
            width=2
        


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

    def add_animal(self, animal: Animal, fence: Fence, ):
        if fence.area >= animal.height * animal.width and fence.habitat == animal.preferred_habitat:
                fence.area -= animal.height * animal.width
                fence.animals.append(animal)
                print(f'{animal.name} aggiunto in {fence}')
        else:
            print(f'{animal.name} non può essere inserito in {fence}')
        
    def remove_animal(self, animal:Animal, fence:Fence, ):
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

    def clean(self,fence: Fence):
        if fence.area == 0:
            return 0.0
        else:
            occupied_area = sum(animal.height * animal.width for animal in fence.animals)
            return occupied_area / fence.area if fence.area != 0 else occupied_area
        



    def __str__(self):
        return f"ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})"
    


class Zoo:
    def __init__(self):
        self.fences:list[Fence] = []
        self.zoo_keepers:list[ZooKeeper] = []


    def describe_zoo(self):
        description ="Guardians:\n"
        for keeper in self.zoo_keepers:
            description +=f"ZooKeeper(name={keeper.name}, surname={keeper.surname}, id={keeper.id})\n"

        description +="Fences:\n"
        for fence in self.fences:
            description +=f"Fence(area={fence.area},temperature={fence.temperature}, habitat={fence.habitat})\nwith animals:\n"
            for animal in fence.animals:
                description +=f"Animal(name={animal.name}, species={animal.species}, age={animal.age})\n"
            description +="#" * 30 + "\n"

        return description


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
    animal1 = Animal(name="Scoiattolo", species="Blabla", age=-1, height=5, width=2, preferred_habitat="Continentale")
    animal2 = Animal(name="Lupo", species="Lupus", age=14, height=8, width=3, preferred_habitat="Continentale")
    #add and remove animal tries
    zoo_keeper.add_animal(animal1, fence, )
    zoo_keeper.add_animal(animal2, fence, )
    zoo_keeper.remove_animal(animal1, fence, )

    zoo_keeper.feed(animal1, fence)

    total_cleaning_time = zoo_keeper.clean(fence)
    print(total_cleaning_time)

    zoo.describe_zoo()
    