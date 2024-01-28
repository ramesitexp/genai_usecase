import sqlite3


#connect to sqlite

connection=sqlite3.connect("student.db")

#Create a cursor object to insert record, create table, retrieve 
cursor=connection.cursor()

#Create the table
table_info="""
create table student(name varchar(25),class varchar(25),section varchar(25), marks int);
"""
cursor.execute(table_info)

#insert some more records
cursor.execute('''insert into student values('Ramesh','Data engineer','A',90)''') 
cursor.execute('''insert into student values('kumar','Data engineer','B',80)''') 
cursor.execute('''insert into student values('Vikas','Data science','A',86)''') 
cursor.execute('''insert into student values('Sushant','Python','B',90)''') 
cursor.execute('''insert into student values('Karupaya','Data science','A',100)''') 
cursor.execute('''insert into student values('sriram','Data engineer','A',90)''') 
cursor.execute('''insert into student values('Arumugam','cloud','A',90)''') 
cursor.execute('''insert into student values('Dinesh','Data engineer','A',100)''') 
cursor.execute('''insert into student values('Hari','Data science','B',70)''') 

##Display all the records 
print("The insert records are")

data=cursor.execute('''select * from student''')

for row in data:
    print(row)
    
##close the connection
connection.commit()
connection.close()