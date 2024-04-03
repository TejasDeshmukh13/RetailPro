from tkinter import *
from PIL import Image , ImageTk
from tkinter import ttk , messagebox
import mysql.connector
import numpy
import matplotlib

class customerClass :
	def __init__(self , root) :
		self.root = root
		self.root.geometry("1150x600+220+130")
		self.root.title("RETAIL PRO")
		self.root.config(bg = "white")
		self.root.focus_force()

		self.db = mysql.connector.connect(
			host = "localhost" ,
			user = "root" ,
			password = "root" ,
			database = "retailers" ,
			port = 3306
		)

		self.cursor = self.db.cursor()

		# ====title====
		self.icon_title = PhotoImage(file = "logo1.png")
		title = Label(self.root , text = "RETAIL PRO" , image = self.icon_title , compound = LEFT ,
		              font = ("times new roman" , 40 , "bold") , bg = "#010c48" , fg = "white" , anchor = "w" ,
		              padx = 20).place(x = 0 , y = 0 , relwidth = 1 , height = 70)

		# ======================================
		# All Variables=======
		self.var_cust_id = StringVar()
		self.var_pname = StringVar()
		self.var_quantity = StringVar()
		self.var_cname = StringVar()
		self.var_amount = StringVar()
		self.var_sale = StringVar()

		# ====title======
		title = Label(self.root , text = "SALES DETAILS" , font = ("goudy old sty;e" , 15) , bg = "#0f4d7d" ,
		              fg = "white").place(x = 50 , y = 100 , width = 1000)


root=Tk()
obj=customerClass(root)
root.mainloop()