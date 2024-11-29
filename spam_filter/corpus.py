import os

class Corpus:
    def __init__(self, dirpath):
        self.dirpath = dirpath
        
    def emails(self):
        for filename in os.listdir(self.dirpath):
            if not filename.startswith("!"):
                filepath = os.path.join(self.dirpath, filename)
                if os.path.isfile(filepath):
                    with open(filepath, 'r', encoding='utf-8') as file:
                        yield filename, file.read()
