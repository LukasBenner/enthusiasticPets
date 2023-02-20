import string


class FileHandler:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        file = open(self.filepath, "r")
        for line in file:
            print(line)
        file.close()

    def write(self, content: string):
        file = open(self.filepath, "w")
        file.write(content)
        file.close()

    def append(self, content: string):
        file = open(self.filepath, "a")
        file.write(content)
        file.close()

