'''def a_patter():
    for row in range(7):
        for col in range(5):
            if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
                print("* ",end="")
            else:
                print(end="  ")
        print()
a_patter()'''
'''
def p_patter():
    for row in range(7):
        for col in range(5):
            if col==0 or (col==4 and (row==1 or row==2)) or (row==0 or row==3) and col!=4:
                print("* ",end="")
            else:
                print(end=" ")
        print()
p_patter()'''

##def heart_pattern():
##    for row in range(6):
##        for col in range(7):
##            if (row ==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
##                print("*",end="")
##            else:
##                print(" ",end="")
##        print()
##
##heart_pattern()

##
##def p_patter():
##    for row in range(7):
##        for col in range(5):
##            if col==0 or (col==4 and (row==1 or row==2)) or (row==0 or row==3) and col!=4:
##                print("*",end="")
##            else:
##                print(end=" ")
##        print()
##p_patter()
##
##def r_pattern():
##    for row in range(7):
##        for col in range(5):
##            if col ==0 or (col==4 and (row!=0 and row!=3)) or ((row==0 or row==3) and (col>0 and col<4)):
##                print("*",end="")
##            else:
##                print(" ",end="")
##        print()
##
##r_pattern()
##
##def a_patter():
##    for row in range(7):
##        for col in range(5):
##            if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
##                print("*",end="")
##            else:
##                print(end=" ")
##        print()
##a_patter()

def a_pattern():
    for row in range(5):
        for col in range(7):
            if (row==0 and col==3) or (row==1 and (col==2) \
                                       or (row==1 and (col==4))) \
                                       or (row==2 and (col<6 and col>0)) \
                                       or (row==3 and (col==0) \
                                        or (row==3 and col==6)):
                print("*",end="")
            else:
                print(" ",end="")
        print()

a_pattern()

