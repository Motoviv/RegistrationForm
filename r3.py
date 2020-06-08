from tkinter import *
t=Tk()
t.geometry("600x400")
t.title("STUDENT INFORMATION")
t.resizable(0,0)#cant resizable
def home():
    f1=Frame(bg="#091e42")
    f1.place(x=0,y=0,width=600,height=400)
    b1=Button(f1,text="LOGIN")
    b1.place(x=220,y=100,width=80,height=40)
    b2=Button(f1,text="REGISTER")
    b2.place(x=310,y=100,width=80,height=40)

home()


t.mainloop()