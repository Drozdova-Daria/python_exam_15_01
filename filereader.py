class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "r")
        for _ in range(1):
            next(self.file)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()