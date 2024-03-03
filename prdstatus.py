from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
class prdstatusClass:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1150x600+220+130")
       self.root.title("RETAIL PRO")
       self.root.config(bg="#ADD8E6")
       self.root.focus_force()

       #====title====
       self.icon_title=PhotoImage(file="logo1.png")
       title=Label(self.root,text="RETAIL PRO",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
       self.var_product_id=StringVar()
       self.var_pname=StringVar()
       self.var_sprice=StringVar()
       self.var_pprice=StringVar()
       self.var_svalue=StringVar()
       self.var_sq=StringVar()
       
       title=Label(self.root,text="PRODUCT STATUS",font=("goudy old sty;e",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)

       lbl_productid=Label(self.root,text="Product ID",font=("goudy old sty;e",15),bg="#ADD8E6").place(x=50,y=150)
       lbl_productid=Label(self.root,text="",font=("goudy old sty;e",15),bg="lightyellow").place(x=190,y=150,width=200)

       lbl_pname=Label(self.root,text="Product Name",font=("goudy old sty;e",15),bg="#ADD8E6").place(x=50,y=220)
       txt_pname=Entry(self.root,text="",font=("goudy old sty;e",15),bg="lightyellow").place(x=190,y=220,width=200)
    
       lbl_price=Label(self.root,text="Sales Price",font=("goudy old sty;e",15),bg="#ADD8E6").place(x=50,y=290)
       txt_price=Entry(self.root,text="",font=("goudy old sty;e",15),bg="lightyellow").place(x=190,y=290,width=200)

       lbl_pprice=Label(self.root,text="Purchase Price",font=("goudy old sty;e",15),bg="#ADD8E6").place(x=50,y=370)
       txt_pprice=Entry(self.root,textvariable=self.var_pprice,font=("goudy old sty;e",15),bg="lightyellow").place(x=190,y=370,width=200)

       lbl_value=Label(self.root,text="Stock value",font=("goudy old sty;e",15),bg="#ADD8E6").place(x=600,y=150)
       lbl_value=Label(self.root,text="",font=("goudy old sty;e",15),bg="lightyellow").place(x=750,y=150,width=200)

       lbl_qnty=Label(self.root,text="Stock Quantity",font=("goudy old sty;e",15),bg="#ADD8E6").place(x=600,y=220)
       lbl_qnty=Label(self.root,text="",font=("goudy old sty;e",15),bg="lightyellow").place(x=750,y=220,width=200)



root=Tk()       
obj=prdstatusClass(root)
root.mainloop()