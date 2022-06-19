#conding:utf-8

class Countlist:
	def __init__(self,*args):
		self.values = [x for x in args]
		self.count = {}.fromkeys(range(len(self.values)),0)
	def __len__(sefl):
		return len(self.values)
	def __getitem__(self,key):
		self.count[key]+=1
		return self.values[key]

a = Countlist(1,2,3)
print a[2]
print a.count