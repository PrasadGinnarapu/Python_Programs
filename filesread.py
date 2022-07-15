

def validuser(fileopen):
    def validate(user):
        l = ['prasad', 'sandeep']
        if user in l:
            return fileopen(user)
        else:
            return "sorry you are not a valid user"
    return validate



@validuser
def fileopen(user):
    return f"hello {user} opening file"
res = fileopen(input("Enter name: "))
print(res)









##with open('readplusfile2.txt',"a+") as f:
##    f.write('Prasad')
##    print(f.tell())
##    res = f.read()
##    print(res)
