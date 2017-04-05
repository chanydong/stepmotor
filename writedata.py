# writedata.py

f=open("home/kimdongchan/chany/new_file.txt",'w')
for i in range(1,11):
	data = "%d"번째 줄입니다.\n" %i
	f.write(data)
f.close()
