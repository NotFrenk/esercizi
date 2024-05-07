class person:
    def __init__(self,name:str, surname:str, age:int):
        self.name = name
        self.surname = surname
        self.age = age
lorenzo=person("lorenzo", "maggi", 24)
print(f"nome = {lorenzo.name}, cognome = {lorenzo.surname}, età = {lorenzo.age}")