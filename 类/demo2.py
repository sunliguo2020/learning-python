class Student():
    def __init__(self, name, score):
        self._name = name
        self.__score = score

    def say_hi(self):
        print(self._name)
        print(self.__score)


s1 = Student("student1",100)
print(dir(s1))
print(s1._name)
print(s1._Student.__score
         _Student__score)
s1.say_hi()
