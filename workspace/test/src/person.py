#conding:utf-8
from _pyio import __metaclass__

__metaclass__ = type

class Person:
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello,world!I'm %s." %self.name

def function():
    print "I dont"
    
class MemberConter(object):
    members = 0
    def init(self):
        MemberConter.members += 1
    
if __name__ == "__main__":
#     foo = Person()
#     bar = Person()
#     foo.setName("luke")
#     bar.setName("ASnd")
#     foo.greet()
#     bar.greet()
#     print foo.name
#     foo.name = "dssdf"
#     print foo.name
#     foo = Person()
#     foo.setName("foo")
#     print foo.getName()
#     foo.getName = function
#     foo.getName()\
    m1 = MemberConter()
    m1.init()
    print MemberConter().members
    m2 = MemberConter()
    m2.init()
    print MemberConter.members