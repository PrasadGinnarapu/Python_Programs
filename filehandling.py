##import re
##url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
##res = re.findall(r"(\d{4})/(\d{2})/(\d{2})",url)
##print(res)

#output: [('2016', '09', '02')]

#=================================

##a="prasad ginnarapu"
##print(a[::-2])




#Write a Python program to add and delete a specific item from a given doubly linked list.

   
##a =1
##b = 0
##print(any(a,b))


##a =16/5
##b=16//5
##print(a+b)

##my_ls = (1,2,3)
##if type(my_ls) is list:
##    print(1==1)


##input_Array = [0,1,8,1,7,1,9,1,2,2,6,2,6,0,1,2,3,5,1]
##
##setdata = set(input_Array)
##print(setdata)
##
##length = len(input_Array)
##output_Array = []
##for i in range(length):
##    if input_Array[i] not in output_Array:
##        output_Array.append(input_Array.count(input_Array[i]))
##print(output_Array)
##    
    
    


##sorted(input_Array)
##length = len(input_Array)
##
##for i in range(length):
##    print(input_Array.count(input_Array[i]))


# Python code to demonstrate
# sort list by frequency
# of elements
##
##from collections import Counter
##
##ini_list = [0,1,8,1,7,1,9,1,2,2,6,2,6,0,1,2,3,5,1]
##result = [item for items, c in Counter(ini_list).most_common() for item in [items] * c]
##print("final list", str(result))

# Python code to demonstrate
# sort list by frequency
# of elements

def solve(nums):
    mp = {}
    for i in set(nums):
        x=nums.count(i)
        try:
            mp[x].append(i)
        except:
            mp[x]=[i]
    ans=[]
    for i in sorted(mp):
        for j in sorted(mp[i], reverse=True):
            ans.extend([j]*i)    
    return ans[::-1]
nums = [0,1,8,1,7,1,9,1,2,2,6,2,6,0,1,2,3,5,1]
print(solve(nums))




































