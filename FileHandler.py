import string
from multiprocessing import Lock

class FileHandler:

    def __init__(self, filepath):
        self.filepath = filepath
        self.lock = Lock()

    def read(self):
        with self.lock:
            file = open(self.filepath, "r")
            for line in file:
                print(line)
            file.close()

    def write(self, content: string):
        with self.lock:
            file = open(self.filepath, "w")
            file.write(content)
            file.close()

    def append(self, content: string):
        with self.lock:
            file = open(self.filepath, "a")
            file.write(content)
            file.close()
