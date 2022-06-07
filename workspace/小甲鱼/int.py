class int(int):
    def __add__(self,other):
        return int.__sub__(self,other)
