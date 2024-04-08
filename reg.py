import ast
from tkinter import*
from tkinter import messagebox
import mysql.connector



window=Tk()
window.title("SignUp")
window.geometry('925x550+300+200')
window.config(bg='#fff')
window.resizable(False,False)

def expentory():
	username=user.get()
	password=enter_code.get()
	confirm_password=confirm_code.get()

	if password==confirm_password:

		try:
			connection = mysql.connector(host="localhost",user="root",password="root", database="retailers")
			cur = connection.cursor()
			connection.close()
		finally:
			messagebox.showinfo('Signup','Successfully sign up')

img = PhotoImage(file='login.png')
Label(window,image=img,bg='white').place(x=50,y=100)

frame=Frame(window,width=450,height=500,bg="white")
frame.place(x=450,y=50)

heading=Label(frame,text='SIGN UP',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI',23,'bold'))
heading.place(x=100,y=-5)

###########------------------------
def on_enter(e):
	user.delete(0,'end')

def on_leave(e):
	name=user.get()
	if name=='':
		user.insert(0,'Username')

def login():
	window = Tk()
	login
	login.mainloop()
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=60)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=87)

#########------------------
def on_enter(e):
	email.delete(0,'end')

def on_leave(e):
	name=email.get()
	if name=='':
		email.insert(0,'Email Id')
email = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
email.place(x=30,y=130)
email.insert(0,'Email Id')
email.bind('<FocusIn>', on_enter)
email.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=157)

#########------------------
def on_enter(e):
	mobile.delete(0,'end')

def on_leave(e):
	name=mobile.get()
	if name=='':
		mobile.insert(0,'Mobile No')
mobile = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
mobile.place(x=30,y=200)
mobile.insert(0,'Mobile No')
mobile.bind('<FocusIn>', on_enter)
mobile.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=227)

#########------------------
def on_enter(e):
	enter_code.delete(0,'end')

def on_leave(e):
	name=enter_code.get()
	if name=='':
		enter_code.insert(0,'Enter Password')
enter_code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
enter_code.place(x=30,y=270)
enter_code.insert(0,'Enter Password')
enter_code.bind('<FocusIn>', on_enter)
enter_code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=297)

#########------------------
def on_enter(e):
	confirm_code.delete(0,'end')

def on_leave(e):
	name=confirm_code.get()
	if name=='':
		confirm_code.insert(0,'Confirm Password')
confirm_code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
confirm_code.place(x=30,y=340)
confirm_code.insert(0,'Confirm Password')
confirm_code.bind('<FocusIn>', on_enter)
confirm_code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=367)

####################------------------------------

Button(frame,width=39,pady=7,text='SIGN UP',bg='#57a1f8',fg='white',border=0,command=expentory).place(x=35,y=400)
label=Label(frame,text="I have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=95,y=440)

sign_in= Button(frame,width=6,text='Sign in',command = login,border=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_in.place(x=215,y=440)



window.mainloop()