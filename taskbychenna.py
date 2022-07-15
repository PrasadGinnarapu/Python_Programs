##s = "prasad"
##data = {}
##lst = []
##for i in s:
##    if s.count(i)>1:
##        data[s.count(i)]=[i]
##    elif s.count(i)==1:
##        lst.append(i)
##        data[s.count(i)]=lst
##print(data)
##lst = [1,2,3]
##for i in range(len(lst)):
##    x = lambda i,y:i+y,lst[i] 
##print(x)
#
##def max_sub_string(string):
##    string.sort(key=len)
##    return string[-1]
##string = "hello prasad hi thisishigheststring".split(' ')
##print(max_sub_string(string))


##string = "hello prasad hi thisishigheststring".split(' ')
##for i in range(len(string)):
##    for j in range(len(string)):
##        if len(string[i])<=len(string[j]):
##            string[i],string[j]=string[j],string[i]
##print(string[0])


string = "well come ojas".split(" ")

new = ''
for i in range(len(string)):
    if string[i] == 'ojas':
        string[i] = 'python'

new = ' '.join(string)
print(new)
