import mysql.connector  


def create_database():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",databse="phone")
        mycursor=mydb.cursor()
        mycursor.execute("use phone")
        print("\t\t\tcreateing PHONENUMBER Table...")
        sql="CREATE TABLE PHONENUMBER(name varchar(30),phoneno int(12) PRIMARY KEY  ,DOB varchar(20),emailid varchar(30),address varchar(50));"
        mycursor.execute(sql)
        mydb.commit()
    except :
        print("")
        print("\t\t\t****Database has already been created****")
        print("")

        
def add_PHONENUMBER():#working 
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="phonebook")
    mycursor=mydb.cursor()
    mycursor.execute("use phonebook;")
    sql="INSERT INTO PHONENUMBER (name,phoneno,DOB,emailid,address)values(%s,%s,%s,%s,%s)"
    phoneno = int(input("\t\tEnter number = "))
    name=input("\t\tEnter name = ")   
    DOB=input("\t\tEnter DOB = ")
    emailid=input("\t\tEnter emailid = ")
    address=input("\t\tEnter address = ")
    val=(name,phoneno,DOB,emailid,address)
    mycursor.execute(sql,val)
    mydb.commit()
    print("")
    print("\t\t\t*****Details Uploaded*****\n")
    

def list_PHONENUMBER(): #working correctly
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="phonebook")
    mycursor=mydb.cursor()
    mycursor.execute("use phonebook;")
    sql="SELECT * from PHONENUMBER"
    mycursor.execute(sql)
    print("\t\t\t\t*****PHONENUMBER details*****")
    print("\n\n\t\t name \t phoneno \t   DOB \t    emailid \t\t address \n")
    print("\t\t------------------------------------------------------------------")
    for i in mycursor :
        print("\t\t",i[0]," ",i[1]," ",i[2]," ",i[3],"   ",i[4],"\n\n")
        
def upDate_PHONENUMBER():#working correctly
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="phonebook")
    mycursor=mydb.cursor()
    mycursor.execute("use phonebook;")
    while True :
        print("\t\t\t*****Enter the details of the person*****\n")
        print("\n\t\t\twhat do you want update in the records \n")
        print("\t\t\t1.NAME")
        print("\t\t\t2.PHONENUMBER")
        print("\t\t\t3.DOB")
        print("\t\t\t4.EMAIL ID ")
        print("\t\t\t5.ADDRESS")
        print("\t\t\t6.EXIT ")
        print("\t\t\t ")
        c = int(input("Pls Enter Your Choice = "))
        PHONENO=int(input("Enter number = "))
        print("\t\t\t*****Enter The Updated Details *****\n")
        
        if c == 1:             
            nname=input("Enter New Name = " )
            sql="update phonenumber set name =%s where phoneno =%s ;"
            val=(nname,PHONENO)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\t\t\t*****Record(s) UPdated*****")
            
        if c == 2:
            nphone=int(input("Enter New Phonenumber = " ))
            sql="update phonenumber set phoneno=%s where phoneno=%s"
            val=(nphone,PHONENO)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\t\t\t*****Record(s) UPdated*****")            
            
        if c == 3:
            ndob=input("Enter New DOB = " )
            sql="update phonenumber set DOB=%s where phoneno=%s"
            val=(ndob,PHONENO)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\t\t\t*****Record(s) UPdated*****")            
            
        if c == 4:            
            nemail=input("Enter New EMAILID = " )
            sql="update phonenumber set emailid=%s where phoneno=%s"
            val=(nemail,PHONENO)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\t\t\t*****Record(s) UPdated*****")
            
        if c == 5:            
            nadd=input("Enter New ADDRESS = " )
            sql="update phonenumber set address=%s where phoneno=%s"
            val=(nadd,PHONENO)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\t\t\t*****Record(s) UPdated*****\n")
        elif c== 6:
            break

def delete_PHONENUMBER():#work correctly
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="phonebook")
    mycursor=mydb.cursor()
    mycursor.execute("use phonebook;")
    nname=input("Enter name : ") 
    sql=("DELETE FROM PHONENUMBER where name= %s")
    val=(nname,)
    mycursor.execute(sql,val)
    mydb.commit()
    print("\t\t\t*****Record(s)deleted*****")
    

def PHONENUMBER():
    while True:
        print("\t\t\t1.Add New PHONENUMBER")
        print("\t\t\t2.List PHONENUMBER")
        print("\t\t\t3.UpDate PHONENUMBER")
        print("\t\t\t4.Delete PHONENUMBER")
        print("\t\t\t5.Back(Main Menu)")
        p=int(input("\t\tEnter You Choice = "))
        if p==1:
            add_PHONENUMBER()
        elif p==2:
            list_PHONENUMBER()
        elif p==3:
            upDate_PHONENUMBER()
        elif p==4:
            delete_PHONENUMBER()
        elif p==5:
            break
        else:
            print("invalid choice")
print("\t\t\t****PHONEBOOK DATABASE****")
print("\t\t\tUsing PHONEBOOK DATABASE\n") 
while True :
    
    print("\t\tSelect the choices give below")
    print("\t\t1.PHONENUMBER")
    print("\t\t2.database setup")
    print("\t\t3.EXIT\n")
    n=int(input("enter your choice[1-3] = "))
    if n==1:
        PHONENUMBER()
    if n==2:
        create_database()
    if n==3:
        break
    
        
    



    
    
