import time

class FileManager:

    def __init__(self, name_file:str, mode:str):
        self.name_file = name_file
        self.mode = mode
    
    def __enter__(self):

        self.wrapper_file = open(self.name_file, self.mode)

        return self.wrapper_file

    def __exit__ (self, exc_type, exc_value, traceback):

        self.wrapper_file.close()

with FileManager(name_file="prova.txt", mode='w') as file:
    file.write('cioa')

class Timer:
    def __enter__(self):
        self.time = time.time()

    def __exit__ (self, exc_type, exc_value, traceback):
        print(f'time = {time.time() - self.time}')
        return False
    


