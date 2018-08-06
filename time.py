#this is a timer
import gui
import time
count = 0
a = int(input('time'))
while (count < a):
	count_now = a - count
	print(count_now)
	time.sleep(1)
	count += 1

print('done')