from operator import call
from tkinter import *
from PIL import Image, ImageTk
from subprocess import call
import subprocess




class Home:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x740+220+130")
        self.root.config(bg="black")

        self.icon_title = PhotoImage(file="bg.png")
        Label(root, image=self.icon_title, bg='gray').place(x=0, y=0)

        title = Label(self.root, text="RETAIL PRO", font=("times new roman", 50, "bold"), fg="dark blue", anchor="w",
                      padx=20).place(x=950, y=10, relwidth=0.315, height=70)

        self.icon_side = PhotoImage(file="side.png")
        btn_next = Button(text="Click Here", command=self.reg, image=self.icon_side, compound=LEFT, padx=3, anchor="w",
                          font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=BOTTOM,
                                                                                                       fill=X)
    def reg(self):
        self.root.destroy()
        subprocess.run(['python', 'reg.py'])



root = Tk()
obj = Home(root)
root.mainloop()