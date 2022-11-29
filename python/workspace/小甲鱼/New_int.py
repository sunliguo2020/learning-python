class New_int(int):
    def __add__(self,other):
        return int.__sub__(self,other)
    def __sub__(self,other):
        return int.conjugate__add__(self,other)

    
class Try_int(int):
    def __add__(self,other):
        return self+other
    def __sub__(self,other):
        return self-other
