class Room:
    def __init__(self, id:str, floor: int, seats:int):
        self.id=id
        self.floor=floor
        self.seats=seats


    def get_floor(self):
        return self.floor
    
    def get_seats(self):
        return self.seats
    
    def get_id(self):
        return self.id

    def __str__(self):
        return f'room(id={self,id}, floor={self.floor}, seats={self.seats})'


class Building:
    def __init__(self, name:str, address:str, num_floors:int,):
        self.name=name
        self.address=address
        self.num_floors=num_floors
        self.rooms= []

    def get_num_floors(self):
        return self.num_floors
    
    def get_rooms(self):
        return self.rooms
    
    def add_room(self, room:Room):
        if room not in self.rooms\
        and room.get_floor() <= self.get_num_floors():
            self.rooms.append(room)


    def __str__(self):
        return f'{self.name.capirtalize()} @ {self.address}'
    

smi = Building(name='SMI', address='via sierra nevada ', num_floors=5)
smi.add_room(Room(id='666', floors=3, seats=32))
print(smi.get_rooms())
        