##string = "hello this is my sweet name"
##res = string.split()
##for i in res:
##    if len(i)%2==0:
##        print(i,len(i))

##string1="PAY" 
##string2="HAPPY" 
##result=[] 
##if(len(string1) < len(string2)): 
##	for i in string1: 
##		if(i in string2): 
##			result.append(i) 
##else: 
##	for i in string2: 
##		if(i in string1): 
##			result.append(i) 
##print("Common character are:",*result)


##str1 = 'my name is my name'
##dict1={}
##for i in set(str1):
##    dict1[i]=str1.count(i)
##print(dict1)
##dct=sorted(dict1)
##print(dct)

# Insertion sort in Python

##
##def insertionSort(array):
##
##    for step in range(1, len(array)):
##        key = array[step]
##        j = step - 1
##        
##        # Compare key with each element on the left of it until an element smaller than it is found
##        # For descending order, change key<array[j] to key>array[j].        
##        while j >= 0 and key < array[j]:
##            array[j + 1] = array[j]
##            j = j - 1
##        
##        # Place key at after the element just smaller than it.
##        array[j + 1] = key
##
##
##data = [0,1,0,1,0,0,1]
##insertionSort(data)
##print('Sorted Array in Ascending Order:')
##print(data)    


##class A:
##  def method(self):
##    print("A.method() called")
##
##class B(A):
##    def method(self):
##         super().method()
##         print("B.method() called")
##
## 
##b = B()
##b.method()

##str1 = 'my name is my name'
##dict1={}
##for i in set(str1):
##    dict1[i]=str1.count(i)
##print(dict1)
##d=sorted(dict1,key=lambda x:x[-1])
##print(d)
#=====================================
##def fun2(fun1):
##    def inner(x,y):
##        if x=='bhargav' and y=='bhargav':
##            return 'Valid'
##        else:
##            return fun1(x,y)
##    return inner
##
##@fun2
##def fun1(username,password):
##    print('Not valid')
##res=fun1('bhargav','bhargav')
##print(res)
##============================================
##def validate(login):
##    def condition(u, p):
##        if u=='prasad' and p=='1203':
##            return 'Valid'
##        else:
##            return login(u,p)
##    return condition
##
##def login(username, password):
##    return 'Invalid'
##
##s=validate(login)
##res = s('prasad','123')
##print(res)
students = ['Student-1','Student-2','Student-3','Student-4','Student-5','Student-6','Student-7','Student-8','Student-9','Student-10']

weights = [71,70,58,71,60,76,65,58,61,77]

heights = [179,178,160,179,168,167,180,180,170,177]

##res = zip(students, weights, heights)
##for i in res:
##    print(list(i))

##for i in range(len(students)):
##    print(
##    
##

##num = 1212
##
##temp = num
##res = 0
##
##while num>0:
##    dig = num%10
##    res = res*10+dig
##    num=num//10
##if temp == res:
##    print('Polindrome')
##else:
##    print('Not')
#===========================

##x, y = 0,1
##
##while(y < 10):
##    print(x)
##    x,y = y,x+y

    


























