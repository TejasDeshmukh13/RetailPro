from tkinter import*
from PIL import Image,ImageTk
import subprocess
class Expentory:
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
       lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688")
       lbl_menu.pack(side=TOP, fill=X)

       btn_customer = Button(
           LeftMenu,
           text="Customer",
           command=self.customer,
           image=self.icon_side,
           compound=LEFT,
           padx=3,
           anchor="w",
           font=("times new roman", 20, "bold"),
           bg="white",
           bd=3,
           cursor="hand2"
       )
       btn_customer.pack(side=TOP, fill=X)

       btn_supplier = Button(
           LeftMenu,
           text="Supplier",
           command=self.supplier,
           image=self.icon_side,
           compound=LEFT,
           padx=3,
           anchor="w",
           font=("times new roman", 20, "bold"),
           bg="white",
           bd=3,
           cursor="hand2"
       )
       btn_supplier.pack(side=TOP, fill=X)

       btn_inventory = Button(
           LeftMenu,
           text="Inventory",
           command=self.inventory,
           image=self.icon_side,
           compound=LEFT,
           padx=3,
           anchor="w",
           font=("times new roman", 20, "bold"),
           bg="white",
           bd=3,
           cursor="hand2"
       )
       btn_inventory.pack(side=TOP, fill=X)

       btn_product = Button(
           LeftMenu,
           text="Product",
           image=self.icon_side,
           compound=LEFT,
           padx=3,
           anchor="w",
           font=("times new roman", 20, "bold"),
           bg="white",
           bd=3,
           cursor="hand2"
       )
       btn_product.pack(side=TOP, fill=X)

       btn_sales = Button(
           LeftMenu,
           text="Sales",
           image=self.icon_side,
           compound=LEFT,
           padx=3,
           anchor="w",
           font=("times new roman", 20, "bold"),
           bg="white",
           bd=3,
           cursor="hand2"
       )
       btn_sales.pack(side=TOP, fill=X)

       btn_exit = Button(
           LeftMenu,
           text="Exit",
           image=self.icon_side,
           compound=LEFT,
           padx=3,
           anchor="w",
           font=("times new roman", 20, "bold"),
           bg="white",
           bd=3,
           cursor="hand2"
       )
       btn_exit.pack(side=TOP, fill=X)
#=====================================================================

    def customer(self):
        self.root.destroy()
        subprocess.run(['python', 'customer.py'])

      
    def supplier(self):
        self.root.destroy()
        subprocess.run(['python', 'supplier.py'])


    def inventory(self):
        self.root.destroy()
        subprocess.run(['python', 'inventory.py'])


if __name__ == "__main__":
    root = Tk()
    expentory_instance = Expentory(root)
    root.mainloop()