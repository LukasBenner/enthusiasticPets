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

    def read_last_line(self):
        with self.lock:
            file = open(self.filepath, "r")
            last_line = file.readlines()[-1]
            file.close()
        return last_line

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
