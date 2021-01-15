import os


def decorator(func):
    def printiter():
        res = func()
        print(res)
        return res
    return printiter


def print_iter(cls):
    class NewCls:
        def __init__(self):
            self.new_cls = cls

        @decorator
        def __next__(self):
            return next(self.new_class)
    return NewCls


#@print_iter
class DirReader:
    def __iter__(self):
        return self

    def __init__(self, directory):
        self.directory = directory
        self.file = []
        self.index = 0
        for d, dirs, files in os.walk(self.directory):
            for f in files:
                filename, file_extention = os.path.splitext(f)
                if not file_extention:
                    self.file.append(os.path.join(d, f))

    def __next__(self):
        if self.index < len(self.file):
            self.index = self.index + 1
            return self.file[self.index - 1]
        raise StopIteration