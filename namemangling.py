class Parent:
    def __init__(self, private):
        self.__private = private
    def pmethod(self):
        print('hello')

pObj = Parent('Prasad')
#pObj.pmethod()
#print(pObj._Parent__private)

class Child(Parent):
    def __init__(self):
        print(pObj._Parent__private)
    
cObj = Child()

print(locals())
