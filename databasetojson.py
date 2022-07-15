import pymysql

conn = pymysql.connect(host="localhost",database="testdb", user="root",password="root")
cursor = conn.cursor()
cursor.execute("select DISTINCT domain from newtable")
domains = cursor.fetchall()
data = {}
for i in domains:
    domain = i[0]
    cursor.execute("select * from newtable where score between 0 AND 25 AND domain='{}'".format(domain))
    first_part = cursor.fetchall()
print(first_part)
##    data[domain]={"0-25":[i for i in first_part]}
                  
##    second = cursor.execute("select * from newtable where domain=domain and score between 26 and 50")
##    third = cursor.execute("select * from newtable where domain=domain and score between 51 and 75")
##    fourth = cursor.execute("select * from newtable where domain=domain and score between 76 and 100")
##

    
##cursor.execute("select * from newtable where domain=domain and score between 0 and 25")
##var = cursor.fetchall()
##print(data)

