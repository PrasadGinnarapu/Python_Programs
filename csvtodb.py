import csv
import pymysql
db = pymysql.connect(host='localhost', user='root', password='root')
mycursor = db.cursor()
mycursor.execute('create database if not exists Testdb')
mycursor.execute('use Testdb')
mycursor.execute('create table if not exists Student(id int(10), name varchar(50))')
all_values=[]
with open('data.csv','r') as file:
    res = csv.reader(file,delimiter=',')
    for row in res:
        values = (row[0],row[1])
        all_values.append(values)
query = "INSERT INTO `Student`(`id`,`name`)VALUES(%s,%s)"
mycursor.executemany(query,all_values)
db.commit()
