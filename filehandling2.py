file = open("C:/Users/pg21258/Desktop/writebinary.bin","wb")
file.write(b"This is some binary data")
print(type(file))

file.close()


##file = open("C:/Users/pg21258/Desktop/image.jpg","rb")
##print(file.read())
##file.close()






##file = open("C:/Users/pg21258/Desktop/newfile.txt","a+")
##file.write("This is append and read operation\n")
##file.seek(0)
##print(file.read())
##file.close()

##file = open("C:/Users/pg21258/Desktop/somefile.txt","r")
##print(file.read())
##file.close()



##f = open('C:/Users/pg21258/Desktop/student.txt', mode='a+', encoding = 'utf-8')
##print('File Name:', f.name)
##print('File Mode:', f.mode)
##print('File Readable:', f.readable())
##print('File Writable:', f.writable())
##print('File Closed:', f.closed)
##f.close()
##print('File Closed:', f.closed)


















'''
def string_occurence(string):
    d = {}
    for i in string:
        d[i] = string.count(i)
        a = d.keys()
        b = d.values()
        c = list(zip(a,b))
        for j in c:
            for x in j:
                print(x, end='')
string_occurence("totally")

##t2l2o1a1y1

var = ["abc", "def"]

lst = []
for i in var[-1]:
    lst.append(list(i))
print(lst)

string = "totally"
res = {i:string.count(i) for i in string}
test = sorted(res.values())



##if test[::-1] in res.values():
##    print(res.keys())'''
    


