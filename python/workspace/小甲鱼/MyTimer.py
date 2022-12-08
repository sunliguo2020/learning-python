#coding:utf-8
import time as t

class MyTimer():
	def __init__(self):
		self.unit=['年',"月","天","小时","分","秒"]
		self.prompt = "未开始计时"
		self.lasted = []
		self.begin =0
		self.end= 0

	def __str__(self):
		return self.prompt
	__repr__ = __str__
	
	def __add__(self,other):
		print "总共运行了："
		result = []
		for i in rage(6):
			result.append(self.lasted[i]+other.lasted[i])
			if result[i]:
				prompt +=(str(reult[i])+self.unit[i])				
		return prompt
	#计时开始
	def start(self):
		self.begin = t.localtime()
		print "计时开始--"
	#计时结束
	def stop(self):
		if not self.begin:
			print "提示：请先调用start开始计时"
		else:
			self.end = t.localtime()
			self.__calc()
			print "计时结束"
	#内部方法，计算运行时间
	def __calc(self):
		for index in range(6):
			self.lasted.append(self.end[index]-self.begin[index])
			if self.lasted[index]:
				self.prompt += str(self.lasted[index])+self.unit[index]
		#print self.prompt
		#未下一轮计时初始化变量
		self.begin = 0
		self.end = 0

if __name__ == "__main__":
	mytime = MyTimer()
	mytime.start()
	mytime.stop()
	print mytime