'''from enum import Enum
class Animal(Enum):
    ANT = 1
    BEE = 2
    CAT = 3
    DOG = 4'''
def fun(n):
    if n==0 or n==1:
        return 1
    elif n>1:
        return n * fun(n-1)
USER = int(input('Enter Num: '))
res = fun(USER)
print(res)
