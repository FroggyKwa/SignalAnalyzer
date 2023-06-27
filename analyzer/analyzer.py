class Analyzer:
    def __init__(self, file=None):
        self.file = file
        self.data = None

    def load_file(self, filename):
        with open(filename, 'r') as file:
            print(file.readlines())
