from tkinter import *
from PIL import ImageTk, Image
import os
from PIL import Image, ImageTk
from tkinter import Label, Tk

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1000x700')
        self.window.resizable(1, 1)
        
        self.window.title('Login Page')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#001f3f', width=1000, height=800)
        self.lgn_frame.place(x=150, y=50)
        
        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "WELCOME TO RETAIL PRO"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=500, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\\left.jpg')
        photo = ImageTk.PhotoImage(self.side_image.resize((350, 370)))
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='white')
        self.side_image_label.image = photo
        self.side_image_label.place(x=60, y=150)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=80)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign up", bg="#070805", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=190)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Name", bg="#ADD8E6", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=250)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#ADD8E6", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=650, y=250, width=200)

        self.username_line = Canvas(self.lgn_frame, width=200, height=2.0, bg="#ADD8E6", highlightthickness=0)
        self.username_line.place(x=650, y=275)
        # ===== Username icon =========
        self.username_label = Label(self.lgn_frame, text="Mobile_No", bg="#ADD8E6", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#ADD8E6", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=650, y=300, width=200)

        self.username_line = Canvas(self.lgn_frame, width=200, height=2.0, bg="#ADD8E6", highlightthickness=0)
        self.username_line.place(x=650, y=325)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='SIGN UP', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)
        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
        
        # =========== Sign Up ==================================================
        self.sign_button = Button(self.lgn_frame, text='Business registeration', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#001F3F", fg='white')
        self.sign_button.place(x=570, y=590)

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405")
        self.signup_button_label.place(x=670, y=555, width=111, height=35)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#ADD8E6", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=350)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#ADD8E6", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=650, y=350, width=200)

        self.password_line = Canvas(self.lgn_frame, width=200, height=2.0, bg="#ADD8E6", highlightthickness=0)
        self.password_line.place(x=650, y=375)
        # ======== Password icon ================
     
        # ========= show/hide password ==================================================================
        

    

    
        self.email_label = Label(self.lgn_frame, text="Email_Id", bg="#ADD8E6", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.email_label.place(x=550, y=400)

        self.email_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#ADD8E6", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.email_entry.place(x=650, y=400, width=200)

        self.email_line = Canvas(self.lgn_frame, width=200, height=2.0, bg="#ADD8E6", highlightthickness=0)
        self.email_line.place(x=650, y=420)
        # ===== Username icon =========
       

def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()