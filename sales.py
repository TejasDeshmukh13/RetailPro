from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from datetime import *

class SalesClass(Tk):
    def __init__(self):
        super().__init__()
        self.list_y_purchase = None
        self.list_x_purchase = None
        self.list_y_sales = None
        self.list_x_sales = None
        self.geometry("1150x600+220+130")
        self.title("RETAIL PRO")
        self.config(bg="white")
        self.focus_force()

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="retailers",
            port=3306
        )
        self.cursor = self.db.cursor()

        self.icon_title = PhotoImage(file="logo1.png")
        title = Label(self, text="RETAIL PRO", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w",
                      padx=20).place(x=0, y=0, relwidth=1, height=70)

        title = Label(self, text="SALES DETAILS", font=("goudy old style", 15), bg="#0f4d7d",
                      fg="white").place(x=0, y=100, width=1150)

        self.figure_purchase = Figure(figsize=(6, 4), dpi=100)
        self.axes_purchase = self.figure_purchase.add_subplot(111)

        self.figure_sales = Figure(figsize=(6, 4), dpi=100)
        self.axes_sales = self.figure_sales.add_subplot(111)

        self.figure_canvas_purchase = FigureCanvasTkAgg(self.figure_purchase, self)
        self.figure_canvas_purchase.get_tk_widget().place(x=50, y=140)

        self.figure_canvas_sales = FigureCanvasTkAgg(self.figure_sales, self)
        self.figure_canvas_sales.get_tk_widget().place(x=600, y=140)

        self.load_button = Button(self, text='Load Graph', command=self.load_data)
        self.load_button.place(relx=0.5, rely=0.93, anchor="s")

        NavigationToolbar2Tk(self.figure_canvas_purchase, self)

    def load_data(self) :
        query_purchase = "SELECT `total_price`, `purchase_month` FROM `supplier`"
        query_sales = "SELECT `total_amount`, `sale_month` FROM `customer`"

        # Fetch all data and initialize the lists with zeros for all months
        self.list_y_purchase = [0] * 12
        self.list_y_sales = [0] * 12

        self.cursor.execute(query_purchase)
        data_purchase = self.cursor.fetchall()
        for row in data_purchase :
            month_index = row[1] - 1  # Adjust month index to start from 0
            self.list_y_purchase[month_index] = row[0]

        self.cursor.execute(query_sales)
        data_sales = self.cursor.fetchall()
        for row in data_sales :
            month_index = row[1] - 1  # Adjust month index to start from 0
            self.list_y_sales[month_index] = row[0]

        self.plot_data()

    def plot_data(self):
        self.axes_purchase.clear()
        self.axes_sales.clear()

        months_abbr = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        self.axes_purchase.bar(months_abbr, self.list_y_purchase, color='b')
        self.axes_purchase.set_title('Purchase Details')
        self.axes_purchase.set_xlabel('Month')
        self.axes_purchase.set_ylabel('Price')

        self.axes_sales.bar(months_abbr, self.list_y_sales, color='g')
        self.axes_sales.set_title('Sales Details')
        self.axes_sales.set_xlabel('Month')
        self.axes_sales.set_ylabel('Price')

        self.figure_canvas_purchase.draw()
        self.figure_canvas_sales.draw()

root = SalesClass()
root.mainloop()
