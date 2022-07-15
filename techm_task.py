

class Employee:
    def __init__(self, name):
        self.name = name

with open("Employees.txt","r") as emp:
    for i in emp:
        res = i.split(" ")
        #print('res: ',res)


obj1 = Employee(res[1])
#obj2 = Employee(res[1])
print(obj1.name)
#print(obj2.name)


