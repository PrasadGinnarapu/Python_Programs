import pymysql
import pandas as pd

con = pymysql.connect(host="localhost",
                      user="root",
                      password="root",
                      db="employee")

qry = "select * from student"
res = pd.read_sql(qry,con)

res.to_csv("first.csv")
print(res)
