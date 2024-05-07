class Student:
    def __init__ (self, name:str, studyProgram:str):
        self.name=name
        self.age= None
        self.gender=None
        self.studyProgram=studyProgram

    def set_age(self, new_age:int):
        self.age=new_age

    def set_gender(self,new_gender:str):
        self.gender=new_gender
        

    def __str__(self):
        return f"\nperson\n(name={self.name}\nage={self.age}\ngender={self.gender}\nstudyProgram={self.studyProgram})"


io = Student("Francisco", "Matematica")
persona_destra =Student("gaia","scienze")
persona_sinistra = Student("Lorenzo", "fisica")

io.set_age(20)
io.set_gender("M n")

lista:list[str,int]=[io, persona_destra, persona_sinistra]
for i in lista:
    print(i)