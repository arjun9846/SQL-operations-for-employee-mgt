import mysql.connector


mdb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="arjun@9846",
    database="students"
)
mycr=mdb.cursor()
def list():
    mycr.execute("select * from empdata")
    r=mycr.fetchall()
    for i in r:
        print("Id : ",i(0),"\tName : ",i(1),"\tAge : ",i(2),"\tSalary : ",i(3))

def add():
    id=int(input("Enter Id: "))
    n_name=(input("Enter Name: "))
    n_age=int(input("Enter Age: "))
    n_sal=int(input("Enter Salary: "))
    sql="insert into data values(%s,%s,%s,%s)"
    val=(id,n_name,n_age,n_sal)
    mycr.execute(sql,val)
    mdb.commit()
    print("Employee added successfully!")

def edit():
    id=int(input("Enter Employee Id to edit"))
    n_name=(input("Enter Employee new Name"))
    n_age=(input("Enter Employee new Age"))
    n_sal=(input("Enter Employee new Salary"))
    mycr.execute("update data set name=%s,age=%s,salary=%s where id=%s",(n_name,n_age,n_sal,id))
    mdb.commit()
    print("Employee information updated successfully!")

def delete():
    id=int(input("Enter id of employee to delete: "))
    mycr.execute("delete from data where id=%s",(id,))
    mdb.commit()
    print("Employee deleted successfully!")
c=6
while c!=5:
    print("----------------------------------------------------------------")
    c=int(input("Menu\nPlease select your input \n1.List\n2.Add\n3.Edit\n4.Delete\n5.Exit\nSelect your choice: "))
    if c==1:
        list()
    elif c==2:
        add()
    elif c==3:
        edit()
    elif c==4:
        delete()
if c==5:
    exit()

