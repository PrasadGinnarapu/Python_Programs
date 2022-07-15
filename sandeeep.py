##3.  Write a Python program to check whether a string contains all letters of the alphabet(note:pangram)
##string = 'The quick brown fox jumps over a lazy dog prasad'.lower()
##count=0
##for i in range(97, 97+26):
##    if chr(i) in string:
##        count+=1
##if count==26:
##    print("Pangram")
##else:
##    print("Not Pangram")
##        
##
##




#-------------------------------------------------------------
##words_list = ["Exercises", "Backend","PHP"]
##word_len = []
##for i in words_list:
##    word_len.append((len(i), i))
##word_len.sort()
##print("Smallest word: ",word_len[0][1],"-",word_len[0][0])
##print("Longest word: ",word_len[-1][1],"-",word_len[-1][0])
##    


##
#-------------------------------------------------------------
##user = input('Enter Name: ')
##print("Upper = ",user.upper(),"\nLower = ",user.lower())
#--------------------------------------------------------------
##def multipleoffour(name):
##    if len(name)==4:
##        return name[::-1]
##    return name
##
##name = input('Enter Name: ')
##print(multipleoffour(name))
##import pymysql
##
##pymysql.connect
##
##from faker import Faker
##fake = Faker()
##for i in range(100):
##    print (fake.email())
##    print(fake.country())
##    print(fake.name())
##    print(fake.text())
##    print(fake.latitude(), fake.longitude())
##    print(fake.url())


##
##num = 29
##flag = False
##if num > 1:
##    for i in range(2, num):
##        if (num % i) == 0:
##            flag = True
##            break
##if flag:
##    print(num, "is not a prime number")
##else:
##    print(num, "is a prime number")
##

##string = "hello prasad"
##user = input("Enter Characte
##for i in string:
##    

def myfun(num):
    if num==0:
        return num
    return num+myfun(num-1)

num=10
print(myfun(num))
    

