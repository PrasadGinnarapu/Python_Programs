class Teacher:
    def setid(self, id):
        self.id = id
    def getid(self):
        return self.id
    def setname(self, name):
        self.name = name
    def getname(self):
        return self.name
t = Teacher()

t.setid(21255)
t.setname('Saikrishna')


print(t.getid())
print(t.getname())
print('\n========')

class Student(Teacher):
    def setmarks(self, marks):
        self.marks = marks
    def getmarks(self):
        return self.marks
s = Student()

s.setid(21258)
s.setname('prasad')
s.setmarks(550)

print(s.getid())
print(s.getname())
print(s.getmarks())

        
 
