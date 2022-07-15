##class FibSeries:
##    
##    def fib(self,num):
##
##        if num<=1:
##            return num
##        else:
##            return (fib(num-1)+fib(num-2))
##obj = FibSeries()
##obj.fib(10)
#-----------------
##def fib(num):
##    if num<=1:
##        return num
##    else:
##        return (fib(num-1)+fib(num-2))
##num = int(input("Enter: "))
##for i in range(num):
##    print(fib(i))


for i in range(10):
    b = bin(i)
    if b[2:] == b[-1:-(len(b)-1):-1]:
        print(b,"Polindrome")
