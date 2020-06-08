# click on register then next page will open
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
t=Tk()
t.geometry("600x400")
t.title("STUDENT INFORMATION")
t.resizable(0,0)#cant resizable
# click on login then next page will open

def login():
    f2=Frame(bg="pink")
    f2.place(x=0,y=0,width=600,height=400)

    g1=StringVar()
    g2=StringVar()
#for name
    un=Label(f2,text ="Enter Name",font=("",12),bg="pink",fg="black")
    un.place(x=200,y=50)
    e1=Entry(f2,font=("",12),textvariable=g1)
    e1.place(x=300,y=50,width=120)
#for password
    up=Label(f2,text ="Enter Pass",font=("",12),bg="pink",fg="black")
    up.place(x=200,y=100)
    e2=Entry(f2,font=("",12),show="*",textvariable=g2)
    e2.place(x=300,y=100,width=120)

    def login1():
        db = sqlite3.connect('form.db')
        cr = db.cursor()
        r=cr.execute("select * from regis where UNAME='"+g1.get()+"' AND UPASS='"+g2.get()+"'")
        for r1 in r:
                     mymenu()
                    # messagebox.showinfo('Tittle','WELCOME')
                     break
        else:
            messagebox.showinfo('Tittle', 'Invalid username and Passqword')

        db.commit()
        db.close()
        g1.set("")
        g2.set("")


    b1=Button(f2,text="LOGIN",bg="red",command=login1)
    b1.place(x=260,y=160,width=100,height=40)
    b2=Button(f2,text="HOME",bg="red",command=home)
    b2.place(x=15,y=340,width=100,height=40)
    b3=Button(f2,text="REGISTER",bg="red",command=regis)
    b3.place(x=450,y=340,width=100,height=60)

def mymenu():
           n=ttk.Notebook()
           n.place(x=0,y=0,width=600,height=400)
           inseertdata(n)
           ShowAllData(n)
           SearchData(n)
           UpdateData(n)
           DeleteData(n)
           Logout(n)


def inseertdata(n):
    f4=Frame(bg="grey")
    n.add(f4,text="Insert")

def ShowAllData(n):
    f5 = Frame(bg="grey")
    n.add(f5,text="Show All")

def SearchData(n):
        f6 = Frame(bg="grey")
        n.add(f6,text="Search")

def UpdateData(n):
           f7 = Frame(bg="grey")
           n.add(f7, text="Update")

def DeleteData(n):
    f8 = Frame(bg="grey")
    n.add(f8, text="DeleteData")

def Logout(n):
    f9 = Frame(bg="grey")
    n.add(f9, text="Logout")


def regis():
    f3=Frame(bg="pink")
    f3.place(x=0,y=0,width=600,height=400)
    #variable
    r1=StringVar()
    r2=StringVar()
    r3=StringVar()

#for name
    un=Label(f3,text ="Enter Name",font=("",12),bg="pink",fg="black")
    un.place(x=200,y=50)
    e1=Entry(f3,font=("",12),textvariable=r1)
    e1.place(x=300,y=50,width=120)
#for password
    up=Label(f3,text ="Enter Pass",font=("",12),bg="pink",fg="black")
    up.place(x=200,y=100)
    e2=Entry(f3,font=("",12),show="*",textvariable=r2)
    e2.place(x=300,y=100,width=120)
#for user account
    uc=Label(f3,text ="Enter ContactNo",font=("",12),bg="pink",fg="black")
    uc.place(x=200,y=150)
    e3=Entry(f3,font=("",12),textvariable=r3)
    e3.place(x=300,y=150,width=120)

    def regis1():
                 db= sqlite3.connect('form.db')
                 cr=db.cursor()
                 cr.execute("insert into regis values('"+r1.get()+"','"+r2.get()+"','"+r3.get()+"')")
                 db.commit()
                 db.close()
                 messagebox.showinfo('Tittle','User Registerd')
                 r1.set("")
                 r2.set("")
                 r3.set("")

    b1=Button(f3,text="Register",bg="red",command=regis1)
    b1.place(x=260,y=210,width=100,height=40)
    b2=Button(f3,text="HOME",bg="red",command=home)
    b2.place(x=15,y=340,width=100,height=40)
    b3=Button(f3,text="LOGIN",bg="red",command=login)
    b3.place(x=450,y=340,width=100,height=40)

def home():
    f1=Frame(bg="#091e42")
    f1.place(x=0,y=0,width=600,height=400)
    b1=Button(f1,text="LOGIN",command=login)
    b1.place(x=220,y=100,width=80,height=40)
    b2=Button(f1,text="REGISTER",command=regis)
    b2.place(x=310,y=100,width=80,height=40)

home()


t.mainloop()