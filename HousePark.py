# HousePark

class HousePark:
	lastname = "박"
	def setname(self,name):
		self.fullname = self.lastname + name
	def travel(self,where):
		print("%s,%s,여행을 가다."%(self.fullname,where))


