from tkinter import*
from PIL import Image,ImageTk
from customer import customerClass
from supplier import supplierClass
from Inventory import invetnoryClass
class expentory:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1350x700+0+0")
       self.root.title("RETAIL PRO")
       self.root.config(bg="white")
       #====title====
       self.icon_title=PhotoImage(file="logo1.png")
       title=Label(self.root,text="RETAIL PRO",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

       #======left Menu===
       self.MenuLogo=Image.open("menu_im.png")
       self.MenuLogo=self.MenuLogo.resize((300,200),Image.AFFINE)
       self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

       LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
       LeftMenu.place(x=0,y=102,width=320,height=565)

       lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
       lbl_menuLogo.pack(side=TOP,fill=X)

       self.icon_side=PhotoImage(file="side.png")
       lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
       
       btn_customer=Button(LeftMenu,text="Customer",command=self.customer,image=self.icon_side,compound=LEFT,padx=3,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=3,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       btn_Inventoryr=Button(LeftMenu,text="Inventory",command=self.inventory,image=self.icon_side,compound=LEFT,padx=3,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       btn_product=Button(LeftMenu,text="Product",image=self.icon_side,compound=LEFT,padx=3,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       btn_salesr=Button(LeftMenu,text="Sales",image=self.icon_side,compound=LEFT,padx=3,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=3,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
#=====================================================================

    def customer(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=customerClass(self.new_win)

      
    def supplier(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=supplierClass(self.new_win)


    def inventory(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=invetnoryClass(self.new_win)

root=Tk()         
obj=expentory(root)
root.mainloop()