from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
class customerClass:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1150x600+220+130")
       self.root.title("RETAIL PRO")
       self.root.config(bg="white")
       self.root.focus_force()

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
       btn_add=Button(self.root,text="SAVE",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=199,y=305,width=110,height=28)
       btn_update=Button(self.root,text="UPDATE",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=399,y=305,width=110,height=28)
       btn_delete=Button(self.root,text="DELETE",font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=599,y=305,width=110,height=28)
       btn_clear=Button(self.root,text="CLEAR",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=799,y=305,width=110,height=28)
       
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
       self.CustomerTable.heading("Cid",text="Customer ID")
       self.CustomerTable.heading("Pname",text="Product Name")
       self.CustomerTable.heading("quantity",text="Product quantity")
       self.CustomerTable.heading("Cname",text="Customer Name")
       self.CustomerTable.heading("Amount",text="Total Amount")
       self.CustomerTable.heading("Sale",text="Sale Price")
       self.CustomerTable["show"]="headings"

      
       
       
       self.CustomerTable.pack(fill=BOTH,expand=1)



root=Tk()         
obj=customerClass(root)
root.mainloop()