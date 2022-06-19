'''
Created on 2016-4-19

@author: Administrator
'''

class Student(object):
    
    def __init__(self,name,score):
        self.__name= name
        self.__score=score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def print_score(self):
        print('%s:%s' %(self.__name,self.__score))
    def set_score(self,score):
        if 0<= score <=100:
            self.__score = score
        else:
            raise ValueError('bad score')
    def get_grade(self):
        if self.__score >=90:
            return 'A'
        elif self.__score >=60:
            return 'B'
        else:
            return 'C' 
class Animal(object):
    def run(self):
        print('Anmal is running 0---')
class Dog(Animal):
    def run(self):
        print("Dog is running ----")
class Cat(Animal):
    def run(self):
        print("Cat is running ----")

def run_twice(animal):
    animal.run()
    animal.run()

class Tortoise(Animal):
    def run(self):
        print ("Tortoise is running slowly")
dog = Dog()
dog.run()

run_twice(Tortoise())

run_twice(dog)

print dir(dog)

bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)

bart.print_score()
print bart.get_grade()
'''
bart.age = 89
print bart.age
print type(bart.age)
bart.age
'''
bart.score = 100

print bart.score

bart.set_score(90)
bart.print_score()

#lisa.print_score()