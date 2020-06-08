#delete
# click on register then next page will open
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
t=Tk()
t.geometry("600x400")
t.title("STUDENT INFORMATION")
t.resizable(0,0)#cant resizable
f55=None
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
           insertdata(n)
           ShowAllData(n)
           SearchData(n)
           UpdateData(n)
           DeleteData(n)
           Logout(n)

def insertdata(n):
         f4=Frame(bg="grey")
         n.add(f4,text="Insert")
         i1=StringVar()#to fetch data
         i2=StringVar()
         i3=StringVar()
         i4=StringVar()
         i5=StringVar()

         u1=Label(f4,font=("",11),text="Enter Roll No",)
         u1.place(x=200,y=50)
         e1 =Entry(f4,font=("",11),bg="pink",fg="blue",textvariable=i1)
         e1.place(x=300,y=50,width=130)

         u2=Label(f4,font=("",11),text="Enter Name",)
         u2.place(x=200,y=100)
         e2 =Entry(f4,font=("",11),bg="pink",fg="blue",textvariable=i2)
         e2.place(x=300,y=100,width=130)

         u3=Label(f4,font=("",11),text="Enter Phy",)
         u3.place(x=200,y=150)
         e3 =Entry(f4,font=("",11),bg="pink",fg="blue",textvariable=i3)
         e3.place(x=300,y=150,width=130)

         u4=Label(f4,font=("",11),text="Enter Che",)
         u4.place(x=200,y=200)
         e4 =Entry(f4,font=("",11),bg="pink",fg="blue",textvariable=i4)
         e4.place(x=300,y=200,width=130)

         u5=Label(f4,font=("",11),text="Enter Maths",)
         u5.place(x=200,y=250)
         e5 =Entry(f4,font=("",11),bg="pink",fg="blue",textvariable=i5)
         e5.place(x=300,y=250,width=130)

         def insertdemo1():# to insert data in registretion
                 db = sqlite3.connect('form.db')
                 cr = db.cursor()
                 cr.execute("insert into ins values('"+i1.get()+"','"+i2.get()+"','"+i3.get()+"','"+i4.get()+"','"+i5.get()+"')")
                 db.commit()
                 db.close()
                 messagebox.showinfo('Tittle',' Data   Inserted')
                 i1.set("")
                 i2.set("")
                 i3.set("")
                 i4.set("")
                 i5.set("")
                 ShowAllData1(f55)  #to show all data when inserted

         b1=Button(f4,text="INSERT",command=insertdemo1,bg="red")
         b1.place(x=260,y=310,width=80,height=40)


def ShowAllData(n):
    f5 = Frame(bg="orange")
    n.add(f5,text="Show All")
    global f55 #fetch
    f55=f5
    ShowAllData1(f5)

def ShowAllData1(f5):
    for w in f5.winfo_children():
        w.destroy() #to delete in a proper manner

    u1=Label(f5,text="RNO",font=("",11),bg="#091e42",fg="white")
    u1.place(x=0, y=0, width=120)

    u2=Label(f5,text="NAME",font=("",11),bg="#091e42",fg="white")
    u2.place(x=120, y=0, width=120)

    u3=Label(f5,text="PHY",font=("",11),bg="#091e42",fg="white")
    u3.place(x=240, y=0, width=120)

    u4=Label(f5,text="CHE",font=("",11),bg="#091e42",fg="white")
    u4.place(x=360, y=0, width=120)

    u5=Label(f5,text="MATHS",font=("",11),bg="#091e42",fg="white")
    u5.place(x=480, y=0, width=120)
        #to connect to db to fetch all data

    db=sqlite3.connect('form.db')
    cr=db.cursor()
    r=cr.execute("select * from ins")
    x=0
    y=60
    for r1 in r:
               Label(f5,text=r1[0],font=("", 11),bg="#091e42", fg="white").place(x=x, y=y, width=120)
               x+=120
               Label(f5,text=r1[1],font=("", 11),bg="#091e42", fg="white").place(x=x, y=y, width=120)
               x+=120
               Label(f5,text=r1[2],font=("", 11),bg="#091e42", fg="white").place(x=x, y=y, width=120)
               x+=120
               Label(f5,text=r1[3],font=("", 11),bg="#091e42", fg="white").place(x=x, y=y, width=120)
               x+=120
               Label(f5,text=r1[4],font=("", 11),bg="#091e42", fg="white").place(x=x, y=y, width=120)
               y+=40
               x=0

    db.commit()
    db.close()


def SearchData(n):
        f6 = Frame(bg="#091e42")
        n.add(f6,text="Search")
        s1=StringVar()
 #to search data
        u1 = Label(f6,font=("", 11), text="Enter Roll No" )
        u1.place(x=100,y=50)
        e1=Entry(f6,font=("",11),textvariable=s1)
        e1.place(x=200,y=50,width=110)

        def SearchData1():
              db = sqlite3.connect('form.db')
              cr=db.cursor()
              r=cr.execute("select * from ins where URNO = '"+s1.get()+"'")
              for r1 in r:
                        u3 = Label(f6,font=("", 11), text="Name is" )
                        u3.place(x=200, y=100)
                        u4 = Label(f6,font=("",11),text=r1[1])
                        u4.place(x=300, y=100)

                        u5 = Label(f6,font=("", 11), text="Phy is" )
                        u5.place(x=200, y=150)
                        u6 = Label(f6,font=("",11),text=r1[2])
                        u6.place(x=300, y=150)

                        u7 = Label(f6,font=("", 11), text="CHe is" )
                        u7.place(x=200, y=200)
                        u8 = Label(f6,font=("",11),text=r1[3])
                        u8.place(x=300, y=200)

                        u9 = Label(f6,font=("", 11), text="MATHS" )
                        u9.place(x=200, y=250)
                        u10 = Label(f6,font=("",11),text=r1[4])
                        u10.place(x=300, y=250)


                        break
              else:
                       messagebox.showinfo('Tittle',"Invalid rollno")
                       #when roll no is wrng data is removed
                       u13 = Label(f6,font=("",11),text="",bg="#091e42")
                       u13.place(x=200,y=100,width=300)
                       u14 = Label(f6, font=("", 11),text="",bg="#091e42")
                       u14.place(x=200,y=150,width=300)
                       u15 = Label(f6, font=("", 11),text="",bg="#091e42")
                       u15.place(x=200,y=200,width=300)
                       u16 = Label(f6, font=("", 11),text="",bg="#091e42")
                       u16.place(x=200,y=250,width=300)

              db.commit()
              db.close()

        b1 = Button(f6,text="SEARCH",font=("",11),command=SearchData1)
        b1.place(x=350,y=50,width=130,height=25)



def UpdateData(n):
               f7 = Frame(bg="#091e42")
               n.add(f7, text="Update")
               s1=StringVar()

               # to update data
               u1 = Label(f7, font=("", 11),text="Enter RollNo",bg="#091e42",fg="white")
               u1.place(x=100, y=50)
               e1 = Entry(f7, font=("", 11),textvariable=s1)
               e1.place(x=200, y=50, width=110)

               def UpdateData1():
                   db = sqlite3.connect('form.db')
                   cr = db.cursor()
                   r = cr.execute("select * from ins where URNO ='"+s1.get()+"'")
                   for r1 in r:
                       s2=StringVar()
                       s3=StringVar()
                       s4=StringVar()
                       s5=StringVar()

                       u3 = Label(f7, font=("", 11), text="Name is",bg="#091e42",fg="white")
                       u3.place(x=200, y=100)
                       u4 = Entry(f7, font=("", 11),textvariable=s2,bg="#091e42",fg="white")
                       u4.insert(0,r1[1])
                       u4.place(x=300, y=100)

                       u5 = Label(f7, font=("", 11), text="Phy is",bg="#091e42",fg="white")
                       u5.place(x=200, y=150)
                       u6 = Entry(f7, font=("", 11),textvariable=s3,bg="#091e42",fg="white")
                       u6.insert(0,r1[2])
                       u6.place(x=300, y=150)

                       u7 =Label(f7, font=("", 11), text="CHe is",bg="#091e42",fg="white")
                       u7.place(x=200, y=200)
                       u8 = Entry(f7, font=("",11),textvariable=s4,bg="#091e42",fg="white")
                       u8.insert(0,r1[3])
                       u8.place(x=300, y=200)

                       u9 = Label(f7, font=("", 11), text="MATHS is",bg="#091e42",fg="white")
                       u9.place(x=200, y=250)
                       u10 = Entry(f7, font=("",11),textvariable=s5,bg="#091e42",fg="white")
                       u10.insert(0,r1[4])
                       u10.place(x=300, y=250)

                       def UpdateData2():
                           db = sqlite3.connect('form.db')
                           cr = db.cursor()
                           cr.execute("update ins set UPASS='"+s2.get()+"',UPHY='"+s3.get()+"',UCHE='"+s4.get()+"',UMATHS='"+s5.get()+"' where URNO='"+s1.get()+"'")
                           db.commit()
                           db.close()
                           ShowAllData1(f55)  # to show all data when inserted

                           messagebox.showinfo('Tittle','Data Updated')
                           s1.set("")
                           s2.set("")
                           s3.set("")
                           s4.set("")
                           s5.set("")

                       b11 = Button(f7, font=("", 11), text="Update",command=UpdateData2)
                       b11.place(x=250,y=310,width=80,height=40)


                       break
                   else:
                       messagebox.showinfo('Tittle', "Invalid rollno")
                       # when roll no is wrng data is removed
                       u13 = Label(f7, font=("", 11), text="", bg="#091e42",fg="white")
                       u13.place(x=200, y=100, width=300)
                       u14 = Label(f7, font=("", 11), text="", bg="#091e42",fg="white")
                       u14.place(x=200, y=150, width=300)
                       u15 = Label(f7, font=("", 11), text="", bg="#091e42",fg="white")
                       u15.place(x=200, y=200, width=300)
                       u16 = Label(f7, font=("", 11), text="", bg="#091e42",fg="white")
                       u16.place(x=200, y=250, width=300)

                   db.commit()
                   db.close()

               b1 = Button(f7,text="UPDATE",font=("",11),bg="brown",command=UpdateData1)
               b1.place(x=350, y=50, width=130, height=25)


def DeleteData(n):
    f8 = Frame(bg="grey")
    n.add(f8, text="DeleteData")
    d1=StringVar()

    u1 = Label(f8, font=("", 11), text="Enter RollNo", bg="#091e42", fg="white")
    u1.place(x=100, y=50)
    e1 = Entry(f8, font=("", 11),textvariable=d1)
    e1.place(x=200, y=50, width=110)

    def DeleteData1():
           db = sqlite3.connect('form.db')
           cr = db.cursor()
           cr.execute("delete from ins where URNO ='"+d1.get()+"'")
           db.commit()
           db.close()
           ShowAllData1(f55)
           messagebox.showinfo('Tittle', 'Data Deleted')
           d1.set("")


    b1=Button(f8,text="DELETE",bg="red",command=DeleteData1)
    b1.place(x=350, y=50, width=110)


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