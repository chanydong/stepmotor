# test01.py
sum = 0
f=open("/home/kimdongchan/chany/sample.txt",'r')
lines = f.readlines()
f.close()

total = 0
for line in lines:
	score=int(line)
	total = total + score

average = total / len(lines)

f=open("/home/kimdongchan/chany/result.txt","w")
f.write(str(average))
f.close()
