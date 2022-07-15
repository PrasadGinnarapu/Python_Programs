##def fib(par):
##    x,y = 0,1
##    while(x<par):
##        print(x)
##        x,y=y,x+y
##a = int(input('Enter no: '))
##fib(a)
##
##def binaryPolindrome(number):
##    binary = number[2:]
##    return binary == binary[-1::-1]
##
##print(binaryPolindrome(9))
##
##lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
##upper_value = int(input ("Please, Enter the Upper Range Value: "))  
##  
##print ("The Prime Numbers in the range are: ")  
##for number in range (lower_value, upper_value + 1):  
##    if number > 1:  
##        for i in range (2, number):  
##            if (number % i) == 0:  
##                break  
##        else:  
##            print (number)  




#15. Converting the string into piglatin.
# def piglatinConversion(userStr):
#     vowels = 'aeiouAEIOU'
#     for i in range(len(userStr)):
#         letter = userStr[i] 
#         if :
            
    
    
# if __name__ == '__main__':
#     result = piglatinConversion(input('Enter a String :'))
#     print('Piglatin Conversion: ',result)
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

f = factorial
print(f(5))
    
    
    

