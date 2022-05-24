# import pdb
from datetime import datetime

for i in range(1,16):
	if i%3==0 and i%5==0:
		print('fizzBuzz')

	elif i%3==0:
		print(i,'fizz')

	elif i%5==0:
		print(i,'buzz')

	else:
		print(i)

print(datetime.today().strftime('%A %B %d, %Y %H:%M:%S'))

d = datetime.today().strftime('%A %B %d, %Y %H:%M:%S')

print(d.split()[0])