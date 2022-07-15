
d = {'a':1,'b':2,'c':3,'d':4,'e':5}
d1 = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}

##print(d['a'])   #to Get Value using Key.
##
##print(d.get('a')) #to Get Value using get() method.
##
##print(d.values()) #to get All Values using values() method.
##
##print(d.keys())  #to get All Keys using keys() method.
##
##print(d.items()) #to get all Elements using items() method.

d1 = {'f':6}
d1.update(d)

lst=[]
for i in d1.keys():
    lst.append(ord(i))
lst.sort()

for i in lst:
    for j in d1.keys():
        c = chr(i)
        if c == j:
            
            
            print('{',c,':',d1[j],'}',end='')
##    
##    for k,v in d1.items():
##        if c == k:
##            d1.update[c] = v

##                       #a b c d e f
##         if c == d1[k]:
##             print('yes')

    
##    if chr(i)==d1[c]:
##        print(c)
##        d1.setdefault(chr(i),c)
##print(d1)
##    print(chr(i))



##x = {d1[i]: for i in lst}
##print(x)

##lst1 = [1,2,3]
##lst2 = [4,5,6]
##for i in range(len(lst1)):
##    print(lst1[i])
##    print(lst2[i])
