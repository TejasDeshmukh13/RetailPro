from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox


root=Tk()
root.title('Login')
root.geometry('1250x650+220+130')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file='bg.png')
Label(root,image=img,bg='white').place(x=50,y=100)


root.icon_title=PhotoImage(file="images/logo1.png")
title=Label(root,text="RETAIL PRO",image=root.icon_title,compound=LEFT,font=("times new roman",40,"bold"),fg="black",anchor="w",padx=20).place(x=800,y=0,relwidth=1,height=70)


       

root.mainloop()