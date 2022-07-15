'''
----------------Question No: 5

def sorting_each_row(Elements,n):
    
    for i in range(0,len(Elements),n):
        yield Elements[i:i+n]
try:      
    LengthOfElements = int(input("Enter Length of Elements: "))
    if (LengthOfElements)%3==0:     
        Elements=[]
        n=3
        for Each in range(LengthOfElements):
            Element=int(input("Enter Elements: "))
            Elements.append(Element)
        object_data = sorting_each_row(Elements,n)
        for i in object_data:
            result = sorted(i)
            print(result)
    else:
        print('Invalid Length')
except:
    print("Wrong Input")

'''
'''
----------------Question No: 4
def sorting_oneD_array(SORTED_LIST,n):
    

    for i in range(0,len(SORTED_LIST),n):
        yield SORTED_LIST[i:i+n]
try:      
    LengthOfElements = int(input("Enter Length of Elements: "))
    if (LengthOfElements)%3==0:     
        Elements=[]
        n=3
        for Each in range(LengthOfElements):
            Element=int(input("Enter Elements: "))
            Elements.append(Element)
            SORTED_LIST = sorted(Elements)
        print('Given Input: \n',SORTED_LIST)
        object_data = sorting_oneD_array(SORTED_LIST,n)
        result = list(object_data)
        print('Sorted Array: \n',[sorted(i) for i in result])
    else:
        print('Invalid Length')
except:
    print("Wrong Input")
'''
'''
----------------Question No: 3

def swap_adj_chars(STRING,CHAR):
    NEW_STRING = []
    for i in range(len(STRING)):
        if STRING[i] == CHAR:
            NEW_STRING.pop(i-1)
            STRING[i-1],STRING[i+1] = STRING[i+1],STRING[i-1]
            NEW_STRING.append(STRING[i-1])
            NEW_STRING.append(CHAR)
            NEW_STRING.append(STRING[i+1])
            NEW_STRING.pop(i+1)
        else:
            NEW_STRING.append(STRING[i])
    return ''.join(NEW_STRING)
STRING = list(input('Enter String: '))
CHAR = " "
print(swap_adj_chars(STRING,CHAR))

'''
'''
----------------Question No: 1 & 2
def rotate_image(matrix):
    
  if not matrix or not matrix[0]:
     return []
  n = len(matrix)
  for row in matrix:
     row.reverse()
  for i in range(n):
     for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
  return matrix

matrix = [
[10, 20, 30],
[40, 50, 60],
[70, 80, 90]
]
result = rotate_image(matrix)
for i in result:
    print(i,end='\n')
'''





