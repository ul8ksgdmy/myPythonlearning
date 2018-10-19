from pymongo import MongoClient
from collections import OrderedDict
import datetime
import json
import csv

with open('D:\py\myPythonlearning\py1810\myinfo.json') as f:
    logindata = json.load(f)

host = logindata['host']
port = logindata['port']

client = MongoClient(host, port)

#crate db
db = client['HR']
col = db.EMPLOYEES

#import 5 data by employeeid : from 101 to 105
keys = ['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME', 'EMAIL', 'PHONE_NUMBER', 'HIRE_DATE', 'JOB_ID', 'SALARY', 'COMMISSION_PCT', 'MANAGER_ID', 'DEPARTMENT_ID']

allemployees = []
with open('D:\py\myPythonlearning\py1810\EMPLOYEES.csv', 'r', encoding='utf-8', newline='') as f:
    csvdata = csv.DictReader(f)
    for csvrow in csvdata:
        employees = {}
        for j in keys:
            employees[j] = csvrow[j]
        allemployees.append(employees)

for each in allemployees:
    if int(each['EMPLOYEE_ID']) >= 100 and int(each['EMPLOYEE_ID']) < 106:
        rs =db.EMPLOYEES.insert_one(each)
        print(rs.inserted_id)
        print(int(each['EMPLOYEE_ID']))

# import all data
# for each in allemployees:
#     rs = db.EMPLOYEES.insert_one(each)
#     print(rs.inserted_id)
#     print(int(each['EMPLOYEE_ID']))


#convert string to numerical in mongodb (with Nosql booster)
# salary
# db.EMPLOYEES.find().forEach(function(data){
#     data.SALARY = parseInt(data.SALARY);
#     db.EMPLOYEES.save(data);
# })

#date
# db.EMPLOYEES.find().forEach(function(data) { 
#     data.HIRE_DATE=new Date(data.HIRE_DATE);
#     db.EMPLOYEES.save(data); 
# })


# 조회
# 문제 3
q3 = col.find({'SALARY':{'$gt':15000}}, {'EMPLOYEE_ID':1, 'FIRST_NAME':1, 'SALARY' :1})
for i in q3:
    print(i)

start = datetime.datetime(2005, 1, 1, 12, 30, 30, 125000)
end = datetime.datetime(2005, 5, 31, 12, 30, 30, 125000)

# 문제 4
q4 = col.find({ "HIRE_DATE": {'$gte': start,'$lt': end}})
for i in q4:
    print(i)


param = [{'$group': {'_id': '$JOB_ID', 'total': {'$sum': '$SALARY'}}}, 
         {'$match': {'total': {'$gte': 30000 , '$lte' : 60000}}},
         {'$sort': {'total': -1}}]

# 문제 5
q5 = list(col.aggregate(param))
for i in q5 :
    print(i)