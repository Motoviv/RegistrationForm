# click on login then next page will open
from tkinter import *
t=Tk()
t.geometry("600x400")
t.title("STUDENT INFORMATION")
t.resizable(0,0)#cant resizable
def login():
    f2=Frame(bg="pink")
    f2.place(x=0,y=0,width=600,height=400)
#for name
    un=Label(f2,text ="Enter Name",font=("",12),bg="pink",fg="black")
    un.place(x=200,y=50)
    e1=Entry(f2,font=("",12))
    e1.place(x=300,y=50,width=120)
#for password
    up=Label(f2,text ="Enter Pass",font=("",12),bg="pink",fg="black")
    up.place(x=200,y=100)
    e2=Entry(f2,font=("",12),show="*")
    e2.place(x=300,y=100,width=120)

    b1=Button(f2,text="LOGIN",bg="red")
    b1.place(x=260,y=160,width=100,height=40)
    b2=Button(f2,text="HOME",bg="red",command=home)
    b2.place(x=15,y=340,width=100,height=40)
    b3=Button(f2,text="REGISTER",bg="red")
    b3.place(x=450,y=340,width=100,height=40)






def home():
    f1=Frame(bg="#091e42")
    f1.place(x=0,y=0,width=600,height=400)
    b1=Button(f1,text="LOGIN",command=login)
    b1.place(x=220,y=100,width=80,height=40)
    b2=Button(f1,text="REGISTER")
    b2.place(x=310,y=100,width=80,height=40)

home()


t.mainloop()