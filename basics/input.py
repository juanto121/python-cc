import sys

#name = sys.stdin.readline()
#print('Hey!', name[-7:])

with open('tuples.py','r+') as file:

	print("file mode: %s , file name: %s" %(file.mode,file.name))
	file_txt = file.read()
	print(file_txt)

