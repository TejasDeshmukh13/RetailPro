from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
import subprocess
from datetime import *


class customerClass:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1150x600+220+130")
       self.root.title("RETAIL PRO")
       self.root.config(bg="white")
       self.root.focus_force()

       self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="retailers",
            port=3306
        )

       self.cursor = self.db.cursor()

       #====title====
       self.icon_title=PhotoImage(file="logo1.png")
       title=Label(self.root,text="RETAIL PRO",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

       #======================================
       # All Variables=======
       self.var_cust_id=StringVar()
       self.var_pname=StringVar()
       self.var_quantity=StringVar()
       self.var_cname=StringVar()
       self.var_amount=StringVar()
       self.var_sale=StringVar()
       

       #====title======
       title=Label(self.root,text="CUSTOMER DETAILS",font=("goudy old sty;e",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)

       #=======content=========
       #=========row1==========
       lbl_custide=Label(self.root,text="Product ID",font=("goudy old sty;e",15),bg="white").place(x=50,y=150)
       lbl_pname=Label(self.root,text="Product Name",font=("goudy old sty;e",15),bg="white").place(x=350,y=150)
       lbl_quantity=Label(self.root,text="Product quantity",font=("goudy old sty;e",15),bg="white").place(x=700,y=150)

       txt_custide=Entry(self.root,textvariable=self.var_cust_id,font=("goudy old sty;e",15),bg="lightyellow").place(x=150,y=150,width=180)
       txt_pname=Entry(self.root,textvariable=self.var_pname,font=("goudy old sty;e",15),bg="lightyellow").place(x=500,y=150,width=180)
       txt_quantity=Entry(self.root,textvariable=self.var_quantity,font=("goudy old sty;e",15),bg="lightyellow").place(x=850,y=150,width=180)

         #=========row2==========
       lbl_cname=Label(self.root,text="Cust Name",font=("goudy old sty;e",15),bg="white").place(x=50,y=220)
       lbl_amount=Label(self.root,text="Total Amount",font=("goudy old sty;e",15),bg="white").place(x=350,y=220)
       lbl_sale=Label(self.root,text="Sale Price ",font=("goudy old sty;e",15),bg="white").place(x=700,y=220)

       txt_cname=Entry(self.root,textvariable=self.var_cname,font=("goudy old sty;e",15),bg="lightyellow").place(x=150,y=220,width=180)
       txt_amount=Entry(self.root,textvariable=self.var_amount,font=("goudy old sty;e",15),bg="lightyellow").place(x=500,y=220,width=180)
       txt_sale=Entry(self.root,textvariable=self.var_sale,font=("goudy old sty;e",15),bg="lightyellow").place(x=850,y=220,width=180)

       #==================buttons============
       btn_add=Button(self.root,text="SAVE",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2",command=self.save_data).place(x=450,y=305,width=110,height=28)
       btn_clear=Button(self.root,text="CLEAR",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2",command=self.clear_data).place(x=580,y=305,width=110,height=28)
       btn_back = Button(self.root, text="BACK", font=("goudy old style", 10), bg="blue", fg="white",
                         command=self.dashboard,
                         cursor="hand2").place(x=1050, y=20, width=80, height=25)

       #====================Customer Details=================

       cust_frame=Frame(self.root,bd=3,relief=RIDGE)
       cust_frame.place(x=0,y=350,relwidth=1,height=250)

       scrolly=Scrollbar(cust_frame,orient=VERTICAL)
       scrollX=Scrollbar(cust_frame,orient=HORIZONTAL)

       self.CustomerTable=ttk.Treeview(cust_frame,column=("Cid","Pname","quantity","Cname","Amount","Sale"),yscrollcommand=scrolly.set,xscrollcommand=scrollX.set)       
       scrollX.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)
       scrollX.config(command=self.CustomerTable.xview)
       scrolly.config(command=self.CustomerTable.yview) 
       self.CustomerTable.heading("Cid",text="Product ID")
       self.CustomerTable.heading("Pname",text="Product Name")
       self.CustomerTable.heading("quantity",text="Product quantity")
       self.CustomerTable.heading("Cname",text="Customer Name")
       self.CustomerTable.heading("Amount",text="Total Amount")
       self.CustomerTable.heading("Sale",text="Sale Price")
       self.CustomerTable["show"]="headings"

       self.update_treeview()
       
       
       self.CustomerTable.pack(fill=BOTH,expand=1)
    def clear_data(self):
        # Clearing text in entry widgets
        self.var_cust_id.set("")
        self.var_pname.set("")
        self.var_quantity.set("")
        self.var_cname.set("")
        self.var_amount.set("")
        self.var_sale.set("")

    def save_data(self) :
        try :
            # Fetching data from entry widgets
            product_id = self.var_cust_id.get()
            product_name = self.var_pname.get()
            quantity = self.var_quantity.get()
            cust_name = self.var_cname.get()
            total_amount = self.var_amount.get()
            sale_price = self.var_sale.get()


            # Inserting data into the database
            query = "INSERT INTO customer (product_id, product_name, product_quantity, cust_name, total_amount, sale_price, sale_month) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (product_id , product_name , quantity , cust_name , total_amount , sale_price , datetime.now().month)

            self.cursor.execute(query , values)
            self.db.commit()

            messagebox.showinfo("Success" , "Data saved successfully!")
            self.clear_data()
        except Exception as e :
            messagebox.showerror("Error" , f"Error: {str(e)}")


    def update_treeview(self):
    # Fetch data from the database
        query = "SELECT * FROM customer"
        self.cursor.execute(query)
        data = self.cursor.fetchall()

    # Insert data into the Treeview
        for row in data:
          self.CustomerTable.insert("", "end", values=row)

    def get_month_abbreviation(self , month_number) :
        month_abbr = {
            1 : 'Jan' , 2 : 'Feb' , 3 : 'Mar' , 4 : 'Apr' , 5 : 'May' , 6 : 'Jun' ,
            7 : 'Jul' , 8 : 'Aug' , 9 : 'Sep' , 10 : 'Oct' , 11 : 'Nov' , 12 : 'Dec'
        }
        return month_abbr.get(month_number , '')


    def dashboard(self):
        self.root.destroy()
        subprocess.run(['python', 'dashboard.py'])
root=Tk()         
obj=customerClass(root)
root.mainloop()