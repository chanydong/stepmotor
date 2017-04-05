# HousePark

class HousePark:
	lastname = "박"
	def __init__(self,name):
		self.fullname = self.lastname + name
	def travel(self,where):
		print("%s,%s여행을 가다."%(self.fullname,where))
	def love(self, other):
		print("%s, %s 사랑에 빠졌네"%(self.fullname, other.fullname))
	def __add__(self,other):
		print("%s, %s 결혼 했네" %(self.fullname, other.fullname))


pey = HousePark("응용")
pey.travel("부산")



class HouseKim(HousePark):
	lastname = "김"
	def travel(self,where,day):
		print("%s, %s여행 %s일 가네."%(self.fullname,where,day))



juliet = HouseKim("줄리엣")
juliet.travel("독도",3)

pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.love(juliet)
pey + juliet
