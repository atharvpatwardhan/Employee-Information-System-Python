from tkinter import Label,Button,Tk,StringVar,ttk,END,messagebox
import pymysql

con=pymysql.connect(user='root', password='', host='localhost',db='test') 
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS EMPLOYEES(FIRSTNAME VARCHAR(20),LASTNAME VARCHAR(20),AGE INT(2),BLOODGROUP VARCHAR(2),SALARY INT,EMPID VARCHAR(5) PRIMARY KEY,DESIGNATION VARCHAR(10),GENDER VARCHAR(10));")
#print("Table created successfully")


screen2 = Tk()
screen2.geometry("400x300")
screen2.title("Employee Information Management System")
screen2.configure(bg= "RoyalBlue2")


l1 = Label(screen2,text = "Please Create an Authorization Key : ",bg="gray25",fg="white",width="700",height="3")
l1.pack()

e1 = ttk.Entry(screen2,width="20")
e1.place(x=140,y=100)

def gotomain():
    global authkey1
    authkey1 = e1.get()
    screen2.destroy()



b1 = Button(screen2,text="Ok",width="20",command=gotomain)
b1.place(x=130,y=180)
screen2.mainloop()





#Adding an Employees Data
def info():
    authorization = authkey.get()
    if authorization == authkey1:
        firstname1=firstname.get()
        lastname1=lastname.get()
        age1=age.get()
        salary1=salary.get()
        empid1=empid.get()
        rank1=rank.get()
        bldgrp1=bloodgrp.get()
        gender1=gender.get()

        con=pymysql.connect(user='root', password='', host='localhost',db='test') 
        cur=con.cursor()
        sql = "INSERT INTO EMPLOYEES (FIRSTNAME, LASTNAME,AGE,BLOODGROUP,SALARY,EMPID,DESIGNATION,GENDER) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
        val = (firstname1,lastname1,age1,bldgrp1,salary1,empid1,rank1,gender1)
        cur.execute(sql, val)
        print("Values inserted successfully")

        cur.execute("SELECT * FROM EMPLOYEES")
        r = cur.fetchall()
        messagebox.showinfo("","Record Inserted Successfully")


        
    
        firstname_entry.delete(0,len(firstname1))
        lastname_entry.delete(0,len(lastname1))
        age_entry.delete(0,len(age1))
        salary_entry.delete(0,len(salary1))
        empid_entry.delete(0,len(empid1))
        rank_entry.delete(0,len(rank1))
        authkey_entry.delete(0,END)
        bloodgrp.set("Blood Group")
        gender.set("Male")
    
    else:
        messagebox.showerror("Error","Please enter valid Authorization Key!")

    
    
#Retrieving an Employees Data
def existinguser():

    authorization = authkey.get()

    if authorization == authkey1:
        firstname_entry.delete(0,END)
        lastname_entry.delete(0,END)
        age_entry.delete(0,END)
        salary_entry.delete(0,END)
        empid_entry.delete(0,END)
        rank_entry.delete(0,END)
        authkey_entry.delete(0,END)
        bloodgrp.set("Blood Group")
        gender.set("Male")

        con=pymysql.connect(user='root', password='', host='localhost',db='test') 
        cur=con.cursor()
        sql = "SELECT * FROM EMPLOYEES WHERE EMPID = %s"
        val = empidretrieve_entry.get()
        cur.execute(sql,val)
        r = cur.fetchone()


        firstname_entry.insert(0,r[0])
        lastname_entry.insert(0,r[1])
        age_entry.insert(0,r[2])
        salary_entry.insert(0,r[4])
        empid_entry.insert(0,r[5])
        rank_entry.insert(0,r[6])
        bloodgrp.set(r[3])
        gender.set(r[7])
        empidretrieve_entry.delete(0,END)

    else:
        messagebox.showerror("Error","Please enter valid Authorization Key!")



#Deleting an Employees Data
def deletedata():

    authorization = authkey_entry.get()
    if authorization == authkey1:
        con=pymysql.connect(user='root', password='', host='localhost',db='test') 
        cur=con.cursor()
        sql = "DELETE FROM EMPLOYEES WHERE EMPID = %s"
        val = empidretrieve_entry.get()
        cur.execute(sql,val)
        messagebox.showinfo("","Data Deleted Successfully")
        empidretrieve_entry.delete(0,END)
    else:
        messagebox.showerror("Error","Please enter valid Authorization Key!")



#Displaying all the Records
def displayall():
    authorization = authkey.get()

    if authorization == authkey1:
        con=pymysql.connect(user='root', password='', host='localhost',db='test') 
        cur=con.cursor()
        cur.execute("SELECT * FROM EMPLOYEES")
        r = cur.fetchall()
        messagebox.showinfo("Employee Data ",r)
        authkey_entry.delete(0,END)
    else:
        messagebox.showerror("Error","Please enter valid Authorization Key!")
        


#Exit
def leave():
    quit()
    screen.destroy()

screen = Tk()
screen.geometry("700x700")
screen.title("Employee Information Management System")
screen.configure(bg= "RoyalBlue2")
heading = Label(screen,text = "Employee Information Management System" ,bg="gray25",fg="white",width="700",height="3")
heading.pack()


firstname_text = Label(screen,text="Firstname :" , bg="SteelBlue1")
lastname_text = Label(screen,text="Lastname :", bg="SteelBlue1")
age_text = Label(screen,text="Age :", bg="SteelBlue1")
retrieve_text = Label(screen,text = "Want to work with an exisiting employees data? Use the boxes below :", bg="seashell2")
newusr_text = Label(screen,text = "To enter data for a new employee:",bg="seashell2",width = "30")
salary_text = Label(screen,text = "Salary :", bg="SteelBlue1")
empid_text = Label(screen,text = "Employee ID :",bg="SteelBlue1")
rank_text = Label(screen,text = "Designation :",bg="SteelBlue1")
firstnameretrieve_text = Label(screen,text = "Employee ID: :",bg="SteelBlue1")
authkey_text = Label(screen,text="Authorization Key :" ,bg="SteelBlue1")
bldgrp_text = Label (screen,text = "Blood Group :" ,bg="SteelBlue1")
gender_text = Label(screen,text = "Gender :" ,bg="SteelBlue1")
line_label = Label(screen,bg = "gray25",fg="white",width="700",height="2")
displayouterlabel = Label(screen,text = "Click here to display all the records :",bg = "seashell2")


firstname_text.place(x= 15 , y=100)
lastname_text.place(x= 15 , y=170)
age_text.place(x= 15 , y=240)
retrieve_text.place(x=15, y=480)
newusr_text.place(x=15,y=60)
salary_text.place(x=370 , y=100)
empid_text.place(x=370 ,y=170)
rank_text.place(x=370 ,y=240)
firstnameretrieve_text.place(x=15 ,y=530)
authkey_text.place(x=440 ,y=480)
bldgrp_text.place(x=15 ,y=310)
line_label.place(x=0,y=670)
gender_text.place(x=370 ,y=310)
displayouterlabel.place(x = 340,y = 635)


firstname = StringVar()
firstname_retrieve = StringVar()
lastname = StringVar()
lastname_retrieve = StringVar()
age = StringVar()
salary = StringVar()
empid = StringVar()
rank=StringVar()
authkey = StringVar()
bloodgrp = StringVar()
bloodgrp.set("Blood Group")
Dateofbirth = StringVar()
gender = StringVar()
gender.set("Male")

firstname_entry = ttk.Entry(screen,textvariable = firstname, width = "50")
lastname_entry = ttk.Entry(screen,textvariable = lastname, width = "50")
age_entry = ttk.Entry(screen,textvariable = age, width = "50")
salary_entry = ttk.Entry(screen,textvariable = salary,width = "50")
empid_entry = ttk.Entry(screen,textvariable = empid,width = "50")
rank_entry = ttk.Entry(screen,textvariable = rank,width = "50")
empidretrieve_entry = ttk.Entry(screen,textvariable = firstname_retrieve,width = "50")
authkey_entry = ttk.Entry(screen,textvariable = authkey,width = "20")



bloodgroups = ["A","B","AB","O"]
bldgrp_combo = ttk.Combobox(screen,textvariable = bloodgrp,value = bloodgroups)

genders = ["Male","Female"]
gender_combo = ttk.Combobox(screen,textvariable = gender,value = genders)

firstname_entry.place(x=15 , y=130)
lastname_entry.place(x=15 , y=200)
age_entry.place(x=15 , y=270)
salary_entry.place(x=370 , y=130)
empid_entry.place(x=370 , y=200)
rank_entry.place(x=370 , y=270)
empidretrieve_entry.place(x=100,y=530)
authkey_entry.place(x=550,y=480)
gender_combo.place(x=370,y=340)
bldgrp_combo.place(x=15 ,y=340)

submit = Button(screen,text = "Submit", width = "30",height = "1",command= info , bg = "DodgerBlue2")
submit.place(x=220,y=390)


retrievebutton = Button(screen,text = "Retreive Data",command = existinguser, bg = "DodgerBlue2")
retrievebutton.place(x=120 , y=590)

deletebutton = Button(screen,text = "Delete Data",command=deletedata,bg = "DodgerBlue2")
deletebutton.place(x=250,y=590)

showallbutton = Button(text = "Display all the Records",command = displayall,bg = "DodgerBlue2")
showallbutton.place(x = 550,y = 635)



exit_button = ttk.Button(text = "           Exit           ",command = leave)
exit_button.place(x = 300,y = 673)

screen.mainloop()
