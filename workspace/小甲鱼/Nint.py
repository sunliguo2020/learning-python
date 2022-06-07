class Nint(int):
    def __radd__(self,other):
        return int.__sub__(self,ohter)
