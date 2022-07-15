import pymysql
from faker import Faker
fake = Faker()


mydb = pymysql.connect(host='localhost', user='root', password='root')
mycursor = mydb.cursor()
mycursor.execute('create database if not exists Employee')
mycursor.execute('use Employee')
mycursor.execute('create table if not exists Student(id int(10), name varchar(50))')
idno = 100
name = fake.name()
##sql=("INSERT INTO favourite (number, info) VALUES ({},{})".format(numbers,animals))
query = ("insert into Student(id,name) VALUES({},'{}')".format(idno, name))

mycursor.execute(query)
mydb.commit()
mycursor.execute('select * from student')
res = mycursor.fetchall()
print(res)




##for i in range(100):
##    print (fake.email())
##    print(fake.country())
##    print(fake.name())
##    print(fake.text())
##    print(fake.latitude(), fake.longitude())
##    print(fake.url())
