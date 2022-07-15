##class Pythonclas:
##    def __init__(self, a,b):
##        self.var1 = a
##        self.var2 = b
##    def add(self):
##        return self.var1+self.var2
##obj = Pythonclas('hi','hello')
##print(obj.add())

##s1 = {1,2,3}
##s2 = {4,5,6}
##
###s1.extend(s2)  
##print(s1)


##string = 'Ojas Innovative'
##
##res = reversed(string)
##for i in res:
##    print(i, end='')




##create view viewname as column.... from table where dept ="Python";

##string = 'Ojas Innovative'
##
##
##for i in string:
##    j = i+string
##    print(




##import pickle
# initializing data to be stored in db
##Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 
##'age' : 21, 'pay' : 40000}
##Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
##'age' : 50, 'pay' : 50000}
  
# database
##db = {}
##db['Omkar'] = Omkar
##db['Jagdish'] = Jagdish
##  
### For storing
##b = pickle.dumps(db)       # type(b) gives <class 'bytes'>
##print(b)
  
# For loading
##myEntry = pickle.loads(b)
##print(myEntry)

##import pickle
##  
##def loadData():
##    # for reading also binary mode is important
##    dbfile = open('examplePickle', 'rb')     
##    db = pickle.load(dbfile)
##    for keys in db:
##        print(keys, '=>', db[keys])
##    dbfile.close()
##  
##if __name__ == '__main__':
##    #storeData()
##    loadData()
##


##my_dict = {"a": "PHP", "b":"JAVA", "c":"PYTHON", "d":"NODEJS"}
##obj = enumerate(my_dict, start=1)

##print(dict(obj))
#print([i for i in obj])
##num=12
##print(f"int: {num:d}, hex: {num:x}, oct: {num:o}, bin: {num:b}")
##
#===================Tuple unpacking
##tp = (1,5,7,8)
##(a,b,c,d) = tp
##print(a)
##print(b)
##print(c)
##print(d)


##
##for i in range(1,50+1):
##    if i%5==0:
##       print(i)

class India():
    def capital(self):
        print('India Capital is Delhi')
    def language(self):
        print("India's National language is Hindi")
class China():
    def capital(self):
        print('China Capital is Beiging')
    def language(self):
        print("China's National language is Chinese")
ind = India()
ch = China()
for i in (ind,ch):
    i.capital()
    






