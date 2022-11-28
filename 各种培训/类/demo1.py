class Student():
    def __init__(self, name):
        self.name = name
        return None

    def say_score(self):
        print('self.name', self.score)


s1 = Student("hel")
s1.score = '20'
# locals(s1)
s1.say_score()
s1.name = 'sdfsfsaf'
print(s1.name)
print(dir(s1))
