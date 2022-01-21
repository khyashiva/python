#
import os

import time
print(time.ctime())

import calendar as c
print(c.month(2023, 1))

f = open(r'C:\Users\khyas\Desktop\texts\names.txt','w')
print(os.getcwd())
f.write("hello world")
f.write("hello again")
print(f.closed)
f.close()
print(f.closed)

f = open(r'C:\Users\khyas\Desktop\texts\names.txt')
content = f.read()
print(content)
f.close()








