num = 9
k=0
for i in range(1,5):
    temp=''
    temp = str(num)*i
    k=k+int(temp)
print(k)
    
    
 
    



##def facto(num):
##    '''Factorial of a number without recursion'''
##    factor = 1
##    for i in range(1, num+1):
##        factor = factor*i
##    return factor
##num=int(input('Enter Num: '))
##print(facto(num))
##
##def facto(num):
##    '''Factorial of a number with recursion'''
##    if num==1:
##        return 1
##    else:
##        return num*facto(num-1)
##num=int(input("Enter Num: "))
##print(facto(num))
