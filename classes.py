import random
import string
OTP=''
def otp_generator(size):
    global OTP
    OTP=''.join([random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) for n in range(size)])
    return OTP

print(otp_generator(5))

def validate_user(otp):
    user_input=input("Enter OTP: ")
    if user_input == OTP:
        print("Welcome")
    else:
        print("!Wrong OTP")
validate_user(OTP)
        






'''Name="Prasad"
print(True if Name=='re'  else False)
===========================================
class Students:
    name = input("Enter Student Name: ")
    def __init__(self,age,marks):
        self.age = age
        self.marks = marks
    @staticmethod
    def display_progress(self):
        print("--------",Students.name,"------")
        print(self.age)
        print(self.marks)

student1 = Students()
student1.display_progress()
============================================
class Bird:
    wings = 2
    @classmethod
    def fly(cls, name):
        print('{} flies with {} wings'.format(name, cls.wings))
Bird.fly('parrote')
Bird.fly('hen')'''
