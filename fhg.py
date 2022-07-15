##l1=[1,2,47,9,7]
##l2=[5,7,6,1,4]
####l=[]
####l.append(l1)
####l.append(l2)
####print(l)
##a=[list(i) for i in zip(l1,l2)]
##print(a)

st = 'hello beautiful world prasad' 
st = list('hello beautiful world prasad')
s = " "
st1 = []
for i in range(len(st)):
    if st[i] == s:
        st1.pop(i-1)
        st[i-1],st[i+1] = st[i+1],st[i-1]
        st1.append(st[i-1])
        st1.append(s)
        st1.append(st[i+1])
        st1.pop(i+1)
    else:
        st1.append(st[i])
print(''.join(st1))    
