# Tkinter 

from tkinter import*
import mysql.connector
import tkinter.messagebox as msg

def create_conn() :
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "python_2"
    )
    
def insert_data():
    if e_fname.get() == "" or e_lname.get() == "" or e_email.get() == "" or e_mobile.get() == "" :
        msg.showinfo("Insert Status","All fields are Mandatory")
        
    else :
        conn = create_conn()
        cursor = conn.cursor()
        query = "insert into user(f_name,l_name,email,mobile) values(%s,%s,%s,%s)"
        args = (e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Insert status","Data Inserted Successfully")
        
def search_data():
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')
    if e_id.get()=="":
        msg.showinfo("search status","ID is mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="select * from user where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
            e_fname.insert(0,row[0][1])
            e_lname.insert(0,row[0][2])
            e_email.insert(0,row[0][3])
            e_mobile.insert(0,row[0][4])
            
        else :
            msg.showinfo("search Status","ID not found")
            
        conn.close()
            
         

root=Tk()
root.geometry("350x370")
root.title("My Tkinter Example")
root.resizable(width=False,height=False)

l_id=Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname=Label(root,text="FIRST NAME")
l_fname.place(x=50,y=100)

l_lname=Label(root,text="LAST NAME")
l_lname.place(x=50,y=150)

l_email=Label(root,text="EMAIL")
l_email.place(x=50,y=200)

l_mobile=Label(root,text="MOBILE")
l_mobile.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_email=Entry(root)
e_email.place(x=150,y=200)

e_mobile=Entry(root)
e_mobile.place(x=150,y=250)

insert=Button(root,text="INSERT",bg="black",fg="white",font=("forte",12),command=insert_data)
insert.place(x=20,y=300)

insert=Button(root,text="SEARCH",bg="black",fg="white",font=("forte",12),command=search_data)
insert.place(x=95,y=300)

insert=Button(root,text="UPDATE",bg="black",fg="white",font=("forte",12))
insert.place(x=174,y=300)

insert=Button(root,text="DELETE",bg="black",fg="white",font=("forte",12))
insert.place(x=252,y=300)





root.mainloop()