from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
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
       self.var_supp_name=StringVar()
       self.var_mobile=StringVar()
       self.var_ppid=StringVar()
       self.var_pname=StringVar()
       self.var_pprice=StringVar()
       self.var_tprice=StringVar()
       self.var_searchtxt=StringVar()
       
       #===================searchFrame========
       #==========option========
       lbl_search=Label(self.root,text="Search by Product Id.",bg="white",font=("goudy old style",15))
       lbl_search.place(x=300,y=360)

       txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goundy old style",15),bg="lightyellow").place(x=500,y=360)
       btn_search=Button(self.root,text="Search",command=self.var_searchtxt,font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=750,y=350,width=90)

       #====title======
       title=Label(self.root,text="SUPPLIER DETAILS",font=("goudy old sty;e",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)

       #=======content=========
       #=========row1==========
       lbl_supp_name=Label(self.root,text="Sup.Name",font=("goudy old sty;e",15),bg="white").place(x=50,y=150)
       lbl_mobile=Label(self.root,text="Mobile No",font=("goudy old sty;e",15),bg="white").place(x=350,y=150)
       lbl_ppid=Label(self.root,text="Product Id",font=("goudy old sty;e",15),bg="white").place(x=700,y=150)

       txt_supp_name=Entry(self.root,textvariable=self.var_supp_name,font=("goudy old sty;e",15),bg="lightyellow").place(x=150,y=150,width=180)
       txt_mobile=Entry(self.root,textvariable=self.var_mobile,font=("goudy old sty;e",15),bg="lightyellow").place(x=500,y=150,width=180)
       txt_ppid=Entry(self.root,textvariable=self.var_ppid,font=("goudy old sty;e",15),bg="lightyellow").place(x=850,y=150,width=180)

         #=========row2==========
       lbl_pname=Label(self.root,text="Product Name",font=("goudy old sty;e",15),bg="white").place(x=50,y=220)
       lbl_pprice=Label(self.root,text="Purchase Price",font=("goudy old sty;e",15),bg="white").place(x=350,y=220)
       lbl_tprice=Label(self.root,text="Total price ",font=("goudy old sty;e",15),bg="white").place(x=700,y=220)

       txt_pname=Entry(self.root,textvariable=self.var_pname,font=("goudy old sty;e",15),bg="lightyellow").place(x=150,y=220,width=180)
       txt_pprice=Entry(self.root,textvariable=self.var_pprice,font=("goudy old sty;e",15),bg="lightyellow").place(x=500,y=220,width=180)
       txt_tprice=Entry(self.root,textvariable=self.var_tprice,font=("goudy old sty;e",15),bg="lightyellow").place(x=850,y=220,width=180)

       #==================buttons============
       btn_add=Button(self.root,text="SAVE",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=199,y=305,width=110,height=28)
       btn_update=Button(self.root,text="UPDATE",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=399,y=305,width=110,height=28)
       btn_delete=Button(self.root,text="DELETE",font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=599,y=305,width=110,height=28)
       btn_clear=Button(self.root,text="CLEAR",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=799,y=305,width=110,height=28)
       
       #====================Supplier Details=================
       supp_frame=Frame(self.root,bd=3,relief=RIDGE)
       supp_frame.place(x=0,y=400,relwidth=1,height=400)

       scrolly=Scrollbar(supp_frame,orient=VERTICAL)
       scrollX=Scrollbar(supp_frame,orient=HORIZONTAL)

       self.SupplierTable=ttk.Treeview(supp_frame,column=("sname","smobile","ppid","pname","pprice","tprice"),yscrollcommand=scrolly.set,xscrollcommand=scrollX.set)       
       scrollX.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)
       scrollX.config(command=self.SupplierTable.xview)
       scrolly.config(command=self.SupplierTable.yview) 
       self.SupplierTable.heading("sname",text="Supplier Name")
       self.SupplierTable.heading("smobile",text="Supplier mobile no")
       self.SupplierTable.heading("ppid",text="INvoice No")
       self.SupplierTable.heading("pname",text="Product Name")
       self.SupplierTable.heading("pprice",text="Purchase Price")
       self.SupplierTable.heading("tprice",text="Total Price")
       self.SupplierTable["show"]="headings"
       self.SupplierTable.pack(fill=BOTH,expand=1)
      
root=Tk()         
obj=supplierClass(root)
root.mainloop()