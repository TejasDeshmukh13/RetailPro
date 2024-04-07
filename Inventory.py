from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
import subprocess
class invetnoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1150x600+220+130")
        self.root.title("RETAIL PRO")
        self.root.config(bg="white")
        self.root.focus_force()

        self.db = mysql.connector.connect(
            host = "localhost" ,
            user = "root" ,
            password = "D@zypiyu123" ,
            database = "retailers" ,
            port = 3306
        )
        self.cursor = self.db.cursor()

        #====All Variables====
        self.var_prd_id=StringVar()
        self.var_prd_name=StringVar()
        self.var_stk_quantity=StringVar()

        #====title====
        self.icon_title=PhotoImage(file="logo1.png")
        title=Label(self.root,text="RETAIL PRO",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        btn_back = Button(self.root, text="BACK", font=("goudy old style", 10), bg="blue", fg="white",
                          command=self.dashboard,
                          cursor="hand2").place(x=1050, y=20, width=80, height=25)

        #====invetory====
        inventory_label = Label(self.root, text="INVENTORY DETAILS", font=("times new roman", 15), bg="#0f4d7d", fg="white").place(x=50, y=100, width=1000)

        #InventorySatuts label=====
        status_frame=LabelFrame(self.root,
                                bg="peach puff",
                                relief="ridge"
                                )
        status_frame.place_configure(x=0,
                                     y=160,
                                     width=1150,
                                     relheight=0.1
                                     )
        empty_label = Label(status_frame,
                            bg="peach puff")
        empty_label.grid_configure(sticky="news",
                                   padx=230
                                   )
        inventorystatus_label = Label(status_frame,
                                      text= "Inventory Status : ",
                                      font=("Time New Roman", 13),
                                      bg="lemon chiffon"
                                      )
        inventorystatus_label.grid_configure(column=1,
                                             row=1,
                                             sticky="news",
                                             )
        invtstatus_label=Label(status_frame,
                               text=f"{self.statusquery()}",
                               font=("Time New Roman", 13),
                               bg="lemon chiffon"
                               )
        invtstatus_label.grid_configure(row=1,
                                        column=2,
                                        sticky="news",
                                        padx=5
                                        )

        #showing products in inventory
        inventory_frame=Frame(self.root,bd=3,relief=RIDGE)
        inventory_frame.place(x=0, y=250, relwidth=1, height=400)

        scrolly = Scrollbar(inventory_frame, orient=VERTICAL)
        scrollX = Scrollbar(inventory_frame, orient=HORIZONTAL)

        self.InventoryTable=ttk.Treeview(inventory_frame,
                                         columns=("prd_id",
                                                  "prd_name",
                                                  "stk_quantity")
                                         )
        scrollX.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollX.config(command=self.InventoryTable.xview)
        scrolly.config(command=self.InventoryTable.yview)

        self.InventoryTable.heading("prd_id",text="Product Id")
        self.InventoryTable.heading("prd_name",text="Product Name")
        self.InventoryTable.heading("stk_quantity", text="Stock Quantity")

        self.InventoryTable["show"]="headings"
        self.InventoryTable.pack(fill="both",
                                 expand=1
                                 )
        self.showdata()

    def showdata(self):
        #fetch data from db
        query="SELECT prod_id,prd_name,stock_quantity FROM inventory"
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        #Insert into treeview
        for row in data:
            self.InventoryTable.insert(parent="",index="end",values=row)

    def statusquery(self):
        self.cursor.execute("SELECT count(prod_id) FROM inventory")
        result = self.cursor.fetchone()
        count = result[0] if result else "0"
        return count
    def dashboard(self):
        self.root.destroy()
        subprocess.run(['python', 'dashboard.py'])
root=Tk()
obj=invetnoryClass(root)
root.mainloop()