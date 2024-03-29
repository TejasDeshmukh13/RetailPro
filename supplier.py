from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import mysql.connector
import subprocess


class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1150x600+220+130")
        self.root.title("RETAIL PRO")
        self.root.config(bg="white")
        self.root.focus_force()

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="D@zypiyu123",
            database="retailers",
            port=3306
        )

        self.cursor = self.db.cursor()

        # ====title====
        self.icon_title = PhotoImage(file="logo1.png")
        title = Label(self.root, text="RETAIL PRO", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0,
                                                                                                                 y=0,
                                                                                                                 relwidth=1,
                                                                                                                 height=70)

        # ======================================
        # All Variables=======
        self.var_supp_name = StringVar()
        self.var_mobile = IntVar()
        self.var_ppid = IntVar()
        self.var_pname = StringVar()
        self.var_pprice = IntVar()
        self.var_qntty = IntVar()
        self.var_salesp = IntVar()
        self.var_tprice = IntVar()
        self.var_searchtxt = IntVar()
        self.var_dropdown = IntVar()
        self.var_alert = IntVar()
        self.var_stk_quantity = IntVar()

        # ===================searchFrame========
        # ==========option========
        lbl_search = Label(self.root, text="Search by Product Id.", bg="white", font=("goudy old style", 15))
        lbl_search.place(x=300, y=450)

        txt_search = Entry(self.root, textvariable=self.var_searchtxt, font=("goundy old style", 15),
                           bg="lightyellow").place(x=500, y=450)
        btn_search = Button(self.root, text="Search", command=self.search_data, font=("goudy old style", 15),
                            bg="#0f4d7d", fg="white").place(x=750, y=450, width=90)

        # ====title======
        title = Label(self.root, text="SUPPLIER DETAILS", font=("goudy old sty;e", 15), bg="#0f4d7d", fg="white").place(
            x=50, y=100, width=1000)

        # =======content=========
        # =========row1==========
        lbl_supp_name = Label(self.root, text="Sup.Name", font=("goudy old sty;e", 15), bg="white").place(x=50, y=150)
        lbl_mobile = Label(self.root, text="Mobile No", font=("goudy old sty;e", 15), bg="white").place(x=400, y=150)
        lbl_ppid = Label(self.root, text="Product Id", font=("goudy old sty;e", 15), bg="white").place(x=750, y=150)

        txt_supp_name = Entry(self.root, textvariable=self.var_supp_name, font=("goudy old sty;e", 15),
                              bg="lightyellow").place(x=180, y=150, width=180)
        txt_mobile = Entry(self.root, textvariable=self.var_mobile, font=("goudy old sty;e", 15),
                           bg="lightyellow").place(x=550, y=150, width=180)
        txt_ppid = Entry(self.root, textvariable=self.var_ppid, font=("goudy old sty;e", 15), bg="lightyellow").place(
            x=850, y=150, width=180)

        # =========row2==========
        lbl_pname = Label(self.root, text="Product Name", font=("goudy old sty;e", 15), bg="white").place(x=50, y=220)
        lbl_pprice = Label(self.root, text="Purchase Price", font=("goudy old sty;e", 15), bg="white").place(x=400,
                                                                                                             y=220)
        lbl_qntty = Label(self.root, text="Quantity", font=("goudy old sty;e", 15), bg="white").place(x=750, y=220)
        lbl_salesprice = Label(self.root, text="Sales price", font=("goudy old sty;e", 15), bg="white").place(x=50,
                                                                                                              y=300)
        lbl_tprice = Label(self.root, text="Total price", font=("goudy old sty;e", 15), bg="white").place(x=400, y=300)
        lbl_alert = Label(self.root, text="Low stock alert", font=("goudy old sty;e", 15), bg="white").place(x=750,
                                                                                                             y=300)
        lbl_gst = Label(self.root, text="GST", font=("goudy old sty;e", 15), bg="white").place(x=100, y=370)

        txt_pname = Entry(self.root, textvariable=self.var_pname, font=("goudy old sty;e", 15), bg="lightyellow").place(
            x=180, y=220, width=180)
        txt_pprice = Entry(self.root, textvariable=self.var_pprice, font=("goudy old sty;e", 15),
                           bg="lightyellow").place(x=550, y=220, width=180)
        txt_qntty = Entry(self.root, textvariable=self.var_qntty, font=("goudy old sty;e", 15), bg="lightyellow").place(
            x=850, y=220, width=180)
        txt_salesprice = Entry(self.root, textvariable=self.var_salesp, font=("goudy old sty;e", 15),
                               bg="lightyellow").place(x=180, y=300, width=180)
        txt_tprice = Entry(self.root, textvariable=self.var_tprice, font=("goudy old sty;e", 15),
                           bg="lightyellow").place(x=550, y=300, width=180)
        txt_alert = Entry(self.root, textvariable=self.var_alert, font=("goudy old sty;e", 15), bg="lightyellow").place(
            x=850, y=300, width=100)
        options = ["5", "12", "18", "28"]  # Replace with your desired options
        dropdown = ttk.Combobox(self.root, textvariable=self.var_dropdown, values=options, font=("goudy old style", 15),
                                background="lightyellow")
        dropdown.place(x=180, y=370, width=120)

        # ==================buttons============
        btn_add = Button(self.root, text="SAVE", font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2",
                         command=self.save_data).place(x=450, y=400, width=110, height=28)
        btn_clear = Button(self.root, text="CLEAR", font=("goudy old style", 15), bg="#607d8b", fg="white",
                           cursor="hand2", command=self.clear_data).place(x=580, y=400, width=110, height=28)
        btn_back = Button(self.root, text="BACK", font=("goudy old style", 10), bg="blue", fg="white",command=self.dashboard,
                          cursor="hand2").place(x=1050, y=20, width=80, height=25)

        # ====================Supplier Details=================
        supp_frame = Frame(self.root, bd=3, relief=RIDGE)
        supp_frame.place(x=0, y=500, relwidth=1, height=400)

        scrolly = Scrollbar(supp_frame, orient=VERTICAL)
        scrollX = Scrollbar(supp_frame, orient=HORIZONTAL)

        self.SupplierTable = ttk.Treeview(supp_frame, column=(
        "sname", "smobile", "ppid", "pname", "pprice", "qnty", "sprice", "gst", "tprice"), yscrollcommand=scrolly.set,
                                          xscrollcommand=scrollX.set)
        scrollX.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollX.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        self.SupplierTable.heading("sname", text="Supplier Name")
        self.SupplierTable.heading("smobile", text="Supplier mobile no")
        self.SupplierTable.heading("ppid", text="Product ID")
        self.SupplierTable.heading("pname", text="Product Name")
        self.SupplierTable.heading("pprice", text="Purchase Price")
        self.SupplierTable.heading("qnty", text="Quantity bought")
        self.SupplierTable.heading("sprice", text="sales price")
        self.SupplierTable.heading("gst", text="GST")
        self.SupplierTable.heading("tprice", text="Total Price")

        self.SupplierTable["show"] = "headings"
        self.SupplierTable.pack(fill=BOTH, expand=1)

    def clear_data(self):
        # Clearing text in entry widgets

        self.var_supp_name.set("")
        self.var_mobile.set("")
        self.var_ppid.set("")
        self.var_pname.set("")
        self.var_pprice.set("")
        self.var_qntty.set("")
        self.var_salesp.set("")
        self.var_tprice.set("")
        self.var_searchtxt.set("")
        self.var_dropdown.set("")
        self.var_alert.set("")

    def save_data(self):
        try:
            # Fetching data from entry widgets

            spname = self.var_supp_name.get()
            mobino = self.var_mobile.get()
            prid = self.var_ppid.get()
            prname = self.var_pname.get()
            pprice = self.var_pprice.get()
            qntty = self.var_qntty.get()
            salepr = self.var_salesp.get()
            ttpr = self.var_tprice.get()
            alrt = self.var_alert.get()

            dpd = self.var_dropdown.get()



            # Inserting data into the database
            query1 = "INSERT INTO supplier (supplier_name, mob_no, product_id, product_name, purchase_price, quantity_bought, sales_price_perunit, total_price, gst, low_stockalert) VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s)"
            values1 = (spname, mobino, prid, prname, pprice, qntty, salepr, ttpr, dpd, alrt)

            query2 = "INSERT INTO inventory (prod_id, prd_name,purchase_per_unit,sale_per_unit,stock_quantity,stock_price,GST, low_stk_alert) VALUES (%s,%s, %s, %s, %s, %s, %s,%s)"
            values2 = (prid, prname, pprice, salepr, qntty, ttpr, dpd, alrt)



            self.cursor.execute(query1, values1)
            self.db.commit()

            self.cursor.execute(query2, values2)
            self.db.commit()

            messagebox.showinfo("Success", "Data saved successfully!")
            self.clear_data()

        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    def search_data(self):
        try:
            product_id = self.var_searchtxt.get()

            # Fetching data from the database based on the entered product ID
            query = "SELECT * FROM supplier WHERE product_id = %s"
            self.cursor.execute(query, (product_id,))
            data = self.cursor.fetchall()

            # Clearing existing data in the treeview
            for record in self.SupplierTable.get_children():
                self.SupplierTable.delete(record)

            if data:
                for record in data:
                    # Inserting each record into the treeview
                    self.SupplierTable.insert("", "end", values=record)
            else:
                messagebox.showinfo("Not Found", f"No data found for Product ID: {product_id}")

        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    def dashboard(self):
        self.root.destroy()
        subprocess.run(['python', 'dashboard.py'])
root = Tk()
obj = supplierClass(root)
root.mainloop()