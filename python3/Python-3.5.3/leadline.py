# leadline.py

f=open("/home/kimdongchan/chany/new_file.txt",'r')
lines = f.readlines()
for line in lines:
	print(line)	

f.close()
