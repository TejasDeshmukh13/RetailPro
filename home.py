from tkinter import *
from PIL import Image, ImageTk
from subprocess import call
import subprocess

class Home:
    def __init__(self, root):
        self.root = root
        self.root.config(bg="black")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = 1400
        window_height = 740

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 3  # Adjusted to move the window a bit more up

        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        root.icon_title = PhotoImage(file="logo1.png")
        title = Label(root, text="RETAIL PRO", image=root.icon_title, compound=LEFT, font=("times new roman", 40, "bold"), fg="black", anchor="w", padx=20)
        title.place(x=800, y=0, relwidth=1, height=70)

        self.icon_title = PhotoImage(file="bg.png")
        Label(root, image=self.icon_title, bg='gray').place(x=0, y=0)

        title = Label(self.root, text="RETAIL PRO", font=("times new roman", 50, "bold"), fg="dark blue", anchor="w", padx=20)
        title.place(x=950, y=10, relwidth=0.315, height=70)

        self.icon_side = PhotoImage(file="side.png")
        btn_next = Button(text="Click here to Login", command=self.reg, image=self.icon_side, compound=LEFT, padx=3, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_next.pack(side=BOTTOM, fill=X)

    def reg(self):
        self.root.destroy()
        subprocess.run(['python', 'login.py'])

root = Tk()
obj = Home(root)
root.mainloop()
