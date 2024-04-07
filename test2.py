from datetime import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector

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
            password="root",
            database="retailers",
            port=3306
        )

        self.cursor = self.db.cursor()

        # ====title====
        self.icon_title = PhotoImage(file="logo1.png")
        title = Label(self.root, text="RETAIL PRO", image=self.icon_title, compound=LEFT, font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)

        # ======================================
        # All Variables=======
        self.var_supp_name = StringVar()
        self.var_mobile = StringVar()
        self.var_ppid = StringVar()
        self.var_pname = StringVar()
        self.var_pprice = StringVar()
        self.var_qntty = StringVar()
        self.var_iniqntty = StringVar()
        self.var_salesp = StringVar()
        self.var_tprice = StringVar()
        self.var_searchtxt = StringVar()
        self.var_dropdown = StringVar()
        self.var_alert = StringVar()

        # ===================searchFrame========
        # ==========option========
        lbl_search = Label(self.root, text="Search by Product Id.", bg="white", font=("goudy old style", 15))
        lbl_search.place(x=300, y=450)

        txt_search = Entry(self.root, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow")
        txt_search.place(x=500, y=450)
        btn_search = Button(self.root, text="Search", command=self.check_prod_id, font=("goudy old style", 15), bg="#0f4d7d", fg="white")
        btn_search.place(x=750, y=450, width=90)

        # ====title======
        title = Label(self.root, text="SUPPLIER DETAILS", font=("goudy old style", 15), bg="#0f4d7d", fg="white")
        title.place(x=50, y=100, width=1000)

        # =======content=========
        # ==========row1==========
        lbl_supp_name = Label(self.root, text="Sup.Name", font=("goudy old style", 15), bg="white")
        lbl_supp_name.place(x=50, y=150)
        lbl_mobile = Label(self.root, text="Mobile No", font=("goudy old style", 15), bg="white")
        lbl_mobile.place(x=400, y=150)
        lbl_ppid = Label(self.root, text="Product Id", font=("goudy old style", 15), bg="white")
        lbl_ppid.place(x=750, y=150)

        txt_supp_name = Entry(self.root, textvariable=self.var_supp_name, font=("goudy old style", 15), bg="lightyellow")
        txt_supp_name.place(x=180, y=150, width=180)
        txt_mobile = Entry(self.root, textvariable=self.var_mobile, font=("goudy old style", 15), bg="lightyellow")
        txt_mobile.place(x=550, y=150, width=180)
        txt_ppid = Entry(self.root, textvariable=self.var_ppid, font=("goudy old style", 15), bg="lightyellow")
        txt_ppid.place(x=850, y=150, width=180)

        # ==========row2==========
        lbl_pname = Label(self.root, text="Product Name", font=("goudy old style", 15), bg="white")
        lbl_pname.place(x=50, y=220)
        lbl_pprice = Label(self.root, text="Purchase Price", font=("goudy old style", 15), bg="white")
        lbl_pprice.place(x=400, y=220)
        lbl_qntty = Label(self.root, text="Quantity", font=("goudy old style", 15), bg="white")
        lbl_qntty.place(x=750, y=220)
        lbl_salesprice = Label(self.root, text="Sales price", font=("goudy old style", 15), bg="white")
        lbl_salesprice.place(x=50, y=300)
        lbl_tprice = Label(self.root, text="Total price", font=("goudy old style", 15), bg="white")
        lbl_tprice.place(x=400, y=300)
        lbl_alert = Label(self.root, text="Low stock alert", font=("goudy old style", 15), bg="white")
        lbl_alert.place(x=750, y=300)
        lbl_gst = Label(self.root, text="GST", font=("goudy old style", 15), bg="white")
        lbl_gst.place(x=100, y=370)
        lbl_plus = Label(self.root, text="+", font=("goudy old style", 15), bg="white")
        lbl_plus.place(x=905, y=220, width=10)
        lbl_percentage = Label(self.root, text="%", font=("goudy old style", 15), bg="white")
        lbl_percentage.place(x=305, y=370, width=20)

        txt_pname = Entry(self.root, textvariable=self.var_pname, font=("goudy old style", 15), bg="lightyellow")
        txt_pname.place(x=180, y=220, width=180)
        txt_pprice = Entry(self.root, textvariable=self.var_pprice, font=("goudy old style", 15), bg="lightyellow")
        txt_pprice.place(x=550, y=220, width=180)
        txt_iniqntty = Entry(self.root, textvariable=self.var_iniqntty, font=("goudy old style", 15), bg="lightyellow")
        txt_iniqntty.place(x=850, y=220, width=50)
        txt_qntty = Entry(self.root, textvariable=self.var_qntty, font=("goudy old style", 15), bg="lightyellow")
        txt_qntty.place(x=920, y=220, width=50)
        txt_salesprice = Entry(self.root, textvariable=self.var_salesp, font=("goudy old style", 15), bg="lightyellow")
        txt_salesprice.place(x=180, y=300, width=180)
        txt_tprice = Entry(self.root, textvariable=self.var_tprice, font=("goudy old style", 15), bg="lightyellow")
        txt_tprice.place(x=550, y=300, width=180)
        txt_alert = Entry(self.root, textvariable=self.var_alert, font=("goudy old style", 15), bg="lightyellow")
        txt_alert.place(x=850, y=300, width=100)

        options = [0, 5, 12, 18, 28]  # GST rate
        dropdown = ttk.Combobox(self.root, textvariable=self.var_dropdown, values=options, font=("goudy old style", 15), background="lightyellow")
        dropdown.place(x=180, y=370, width=120)

        # ==================buttons============
        btn_add = Button(self.root, text="SAVE", font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2", command=self.save_data)
        btn_add.place(x=450, y=400, width=120, height=28)

        btn_clear = Button(self.root, text="CLEAR", font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2", command=self.clear_data)
        btn_clear.place(x=710, y=400, width=120, height=28)

        btn_calculate = Button(self.root, text="CALCULATE", font=("goudy old style", 15), bg="deep sky blue", fg="white", cursor="hand2", command=self.calculate_total_price)
        btn_calculate.place(x=580, y=400, width=120, height=28)
        btn_check_id = Button(self.root, text="Check", font=("goudy old style", 12), bg="#4caf50", fg="white", cursor="hand2", command=self.check_prod_id)
        btn_check_id.place(x=850, y=180, width=60, height=25)
        # ====================Supplier Details=================
        supp_frame = Frame(self.root, bd=3, relief=RIDGE)
        supp_frame.place(x=0, y=500, relwidth=1, height=400)

        scrolly = Scrollbar(supp_frame, orient=VERTICAL)
        scrollX = Scrollbar(supp_frame, orient=HORIZONTAL)

        self.SupplierTable = ttk.Treeview(supp_frame, column=("sname", "smobile", "ppid", "pname", "pprice", "qnty", "sprice", "gst", "tprice"), yscrollcommand=scrolly.set, xscrollcommand=scrollX.set)
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
        self.update_treeview()

    def get_month_abbreviation(self, month_number):
        month_abbr = {
            1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
            7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
        }
        return month_abbr.get(month_number, '')

    def update_treeview(self):
        # Clear the existing rows in the Treeview
        for row in self.SupplierTable.get_children():
            self.SupplierTable.delete(row)

        # Fetch data from the database
        query = "SELECT supplier_name, mob_no, product_id, product_name, purchase_price, quantity_bought, sales_price_perunit, gst, total_price, low_stockalert FROM supplier"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        # Insert data into the Treeview
        for row in data:
            self.SupplierTable.insert("", "end", values=row)

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

    def calculate_total_price(self):
        try:
            purchase_price = self.var_pprice.get()
            quantity = self.var_qntty.get()
            gst = self.var_dropdown.get()

            if purchase_price and quantity and gst:
                purchase_price = float(purchase_price)
                quantity = int(quantity)
                # convert it to a decimal
                gst_decimal = float(gst) / 100
                total_price = purchase_price * quantity * (1 + gst_decimal)
                self.var_tprice.set(round(total_price, 2))
            else:
                messagebox.showerror("Error", "Purchase Price, Quantity, and GST must be specified.")
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating total price: {str(e)}")

    def save_data(self) :
        try :
            # Fetching data from entry widgets
            spname = self.var_supp_name.get()
            mobino = self.var_mobile.get()
            prid = int(self.var_ppid.get())
            prname = self.var_pname.get()
            pprice = self.var_pprice.get()
            qntty = self.var_qntty.get()
            salepr = self.var_salesp.get()
            ttpr = self.var_tprice.get()
            alrt = self.var_alert.get()
            dpd = self.var_dropdown.get()

            # Check if the product exists in the inventory
            check_query = "SELECT * FROM inventory WHERE prod_id = %s"
            self.cursor.execute(check_query , (prid ,))
            result = self.cursor.fetchone()

            if not result :
                stock_quantity = self.var_qntty.get()
                stock_price = float(stock_quantity) * float(salepr) + float(stock_quantity) * float(salepr) * (
                        int(dpd) / 100)
                # Insert the new product into the inventory
                insert_query = "INSERT INTO inventory (prod_id, prd_name, purchase_per_unit, sale_per_unit, stock_quantity, stock_price, GST, low_stk_alert) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                insert_values = (prid , prname , pprice , salepr , stock_quantity , stock_price , int(dpd) , alrt)
                self.cursor.execute(insert_query , insert_values)
                self.db.commit()
            else :
                # If the product already exists, update its details
                update_query = "UPDATE inventory SET prd_name = %s, purchase_per_unit = %s, sale_per_unit = %s, stock_quantity = stock_quantity + %s, stock_price = stock_price + %s + %s * %s, GST = %s, low_stk_alert = %s WHERE prod_id = %s"
                # Fetching initial stock quantity from the inventory
                query = "SELECT stock_quantity FROM inventory WHERE prod_id = %s"
                self.cursor.execute(query , (prid ,))
                initial_stock_quantity = self.cursor.fetchone()[0]
                # Calculate total quantity
                total_quantity = initial_stock_quantity + int(qntty)
                # Calculate new stock price
                stock_price = total_quantity * float(salepr) + total_quantity * float(salepr) * (int(dpd) / 100)
                update_values = (prname , pprice , salepr , total_quantity , stock_price , int(dpd) , alrt , prid)
                self.cursor.execute(update_query , update_values)
                self.db.commit()

            # Inserting data into the supplier table
            query = "INSERT INTO supplier (supplier_name, mob_no, product_id, product_name, purchase_price, quantity_bought, sales_price_perunit, gst, total_price, low_stockalert, purchase_month) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (
            spname , mobino , prid , prname , pprice , qntty , salepr , int(dpd) , ttpr , alrt , datetime.now().month)
            self.cursor.execute(query , values)
            self.db.commit()

            messagebox.showinfo("Success" , "Data saved successfully!")
            self.clear_data()
            self.update_treeview()

        except Exception as e :
            messagebox.showerror("Error" , f"Error: {str(e)}")

    def get_month_abbreviation(self , month_number) :
        month_abbr = {
            1 : 'Jan' , 2 : 'Feb' , 3 : 'Mar' , 4 : 'Apr' , 5 : 'May' , 6 : 'Jun' ,
            7 : 'Jul' , 8 : 'Aug' , 9 : 'Sep' , 10 : 'Oct' , 11 : 'Nov' , 12 : 'Dec'
        }
        return month_abbr.get(month_number , '')
    def check_prod_id(self):
        try:
            product_id = self.var_ppid.get()

            # Fetching data from the database based on the entered product ID
            query = "SELECT prd_name, purchase_per_unit, sale_per_unit, stock_quantity, stock_price, GST, low_stk_alert FROM inventory WHERE prod_id = %s"
            self.cursor.execute(query, (product_id,))
            data = self.cursor.fetchone()

            if data:
                # Product ID found in the inventory
                product_name, purchase_price, sale_price, stock_quantity, stock_price, gst, low_stock_alert = data

                # Update the corresponding text fields with the retrieved data
                self.var_pname.set(product_name)
                self.var_pprice.set(purchase_price)
                self.var_salesp.set(sale_price)
                self.var_iniqntty.set(stock_quantity)
                self.var_dropdown.set(gst)
                self.var_alert.set(low_stock_alert)

                messagebox.showinfo("Found", f"Data found for Product ID: {product_id}")
            else:
                # Product ID not found in the inventory
                messagebox.showerror("Not Found", f"No data found for Product ID: {product_id}")
        except Exception as e:
            messagebox.showerror("Fetching Error", f"Error fetching data: {str(e)}")


root = Tk()
obj = supplierClass(root)
root.mainloop()
