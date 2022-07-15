'''lst = [9,3,9]
lst2 = ['prasad','sai','krishna']
d = {}
for i in range(4):
    d[lst[i]]=lst2[i]
print(d)
-------------------------------------
lst1 = [1,2,3]
lst2 = ['A','B','C']
print(dict(zip(lst1, lst2)))
------------------------------
import re

count = 0
for char in re.finditer('l', 'helllo This is prasad '):
    count+=1
if count>=4:
    print('More than 3 occurences')
else:
    print('string is good')
-----------------------------
import re
string = '4234-4512-6874-9654'
re.match(, string
--------------------------
import difflib
text1 = "Prasad is a Trainee Software Engineer."
text2 = "Prasad is a Trainee Software Devoloper"
d = difflib.Differ()
diff = d.compare(text1.splitlines(), text2.splitlines())
print("\n".join(diff))
--------------------------
'''
from datetime import *

#now = datetime.datetime.now().
#today = datetime.datetime.today().year
#date = datetime.datetime()
#print(now)
#print(today)
##res = date.today()
##print(res.strftime('%Y-%B-%d'))
##
##res = timedelta(days=10, hours=10, minutes=10, seconds=60)
##now = datetime.now()
##print(res+now)
##---------------------------
##from threading import Thread
##def myfun(arg):
##    for i in range(10):
##        print(i)
##def myfun2(ar2):
##     for i in range(10):
##        print(i)
##t1 = Thread(target=myfun, args=('prasad',))
##t2 = Thread(target=myfun2, args=('Srinitha',))
##t1.start()
##t2.start()
##
##from threading import Thread
##class Employee(Thread):
##    def run(self, ar):
##        print(ar)
##e= Employee()
##t = Thread(target=e.run, args=('ar',))
##t.start()
##
##from threading import Thread
##class Employee(Thread):
##    def fun(self, ar):
##        print(ar)
##e= Employee()
##t = Thread(target=e.fun, args=('ar',))
##t.start()
##
##from threading import Thread
##class Employee(Thread):
##    def run(self):
##        for i in range(50):
##            print(i)
##e1= Employee()
##e2= Employee()
##e1.start()
##e2.start()

##s1 = {1,2,3,4,5}
##s2 = {4,5,6,7,8}
##print(s1.union(s2))
##print(s1 | s2)
##
##print(s1.intersection(s2))
##
##print(s1.difference(s2))
##
##print(s1.symmetric_difference(s2))
##print(s1 ^ s2)
##
##s1.symmetric_difference_update(s2)
##print(s1)
##
##s1.difference_update(s2)
##print(s1)

#=======================
##def fun(n):
##    a = [0,1]
##    for i in range(n):
##        a.append(a[-1]+a[-2])
##    print(a)
##n=5
##fun(n)
#====================
##def fun(n):
##    a,b = 0,1
##    while a<n:
##        print(a)
##        a,b = b, a+b
##n=10
##fun(n)

import sys
print("When you want exit press Ctrl+d for exit")
sys.stdout.write('hello')

    
















