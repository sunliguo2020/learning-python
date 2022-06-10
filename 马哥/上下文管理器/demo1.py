class FileManager(object):
    def __init__(self, name, mode):
        print("调用__init__方法")
        self.name = name
        self.mode = mode

    def __enter__(self):
        print("调用__enter__方法")
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


if __name__ == '__main__':
    with FileManager("../jiujiu.py", 'r') as file:
        print(type(file))
        print(dir(file))
        print(file.read())
