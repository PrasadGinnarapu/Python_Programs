##import requests
##from requests.auth import HTTPBasicAuth
##response = requests.get('http://saikumarm238.pythonanywhere.com/member',auth=HTTPBasicAuth('admin', '10031'))
##print('Response Code '+ str(response.status_code))
##if response.status_code == 200:
####    print('Login Success: '+response.text)
####    print(response.headers)
####    print(response.url)
##    res = response.json()
##    print(res['members'])


'''lst = ['prasad','naresh']
res=''
for i in lst:
    res=res+''.join(i)
    res=res+','
print(res)'''

'''class A:
    def __init__(self):
        self.a=10
        self.__b=11
        self._c=12
    def method1(self):
        print(self.a)
        print(self.__b)
        print(self._c)
a=A()
a.method1()
print(a.a)
print(a._A__b)
print(a._c)

class B(A):
  def method2(self):
    super().method1()

b=B()
b.method2()'''

#monkey patching
##class A:
##    def m1(self):
##        print("i am from method1")
##    def m2(self):
##        print("i am from method2")
##a=A()
##a.m1=a.m2
##a.m1()

'''
s=[[1,2,3,4],[5,6,7,8]]
k=[]
res=[j for i in s for j in i]
print(res)
--------------------
lst1 = ['sri01234']
lst2=[]
lst3=[]
for i in lst1[0]:
    if i.isdigit():
        lst2.append(i)
    else:
        lst3.append(i)
print(lst2)
print(lst3)
-----------------------
n=6
for i in range(n,0,-1):
    for j in range(i):
        print(i,end="")
    print("")




class Name:
    def __init__(self):
        pass

    @staticmethod
    def display():
        pass
        '''
##
##lst1 = [1,2,3]
##lst2 = [4,5,6]
##lst3 = ['a','b','c']
##var = [j for i in (lst1,lst2) for j in i ]
##print(var)


    



































    
