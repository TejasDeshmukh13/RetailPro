import tkinter as tk
import subprocess

def close_about(about_window):
    about_window.destroy()
    subprocess.run(['python', 'dashboard.py'])

def about_us():
    about_window = tk.Tk()
    about_window.title("About Us")
    screen_width = about_window.winfo_screenwidth()
    screen_height = about_window.winfo_screenheight()

    # Calculate x and y coordinates for the window to be centered
    x_coordinate = (screen_width - 1170) // 2
    y_coordinate = (screen_height - 750) // 2

    about_window.geometry(f"1170x750+{x_coordinate}+{y_coordinate}")
    about_window.configure(bg="#f0f0f0")

    # Create a frame with a gradient background
    gradient_frame = tk.Frame(about_window, bg="#d1e8e7", bd=2, relief=tk.SOLID)
    gradient_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    # About Us Heading
    about_label = tk.Label(gradient_frame, text="About Us", font=("Arial", 24, "bold"), bg="#d1e8e7", fg="#333333")
    about_label.pack(pady=(20, 10))

    # About Us Paragraph
    about_paragraph = tk.Label(gradient_frame,
                               text="Retail Pro is a provider of innovative solutions for retail businesses worldwide. With a focus on simplifying store management, we offer a comprehensive Python-based application designed to meet the unique needs of retailers. Our mission is to empower retail users to make informed financial decisions and manage their products with ease, regardless of their store type.\n\nAt Retail Pro, we specialize in combining Expense Tracker and Inventory Manager functionalities into a single, user-friendly application. Our solution provides retailers with the tools they need to streamline their operations, track spending, and monitor inventory status in real-time. With our specialized approach, we aim to make store management simpler and more efficient for businesses of all sizes.\n\nWhy Choose Us:\n\nTailored Approach: Our application is specifically designed to meet the needs of retail users, offering a specialized solution that addresses common pain points.\nEmpowering Retailers: We empower retailers to take control of their finances and inventory management, enabling them to make informed decisions for their business.\nSeamless Integration: Our application seamlessly integrates Expense Tracker and Inventory Manager functionalities, providing a comprehensive solution for store management.\n\nOur vision is that we envision a future where every retailer has access to the tools they need to succeed. By providing innovative solutions and exceptional service, we strive to be the leading choice for retail businesses seeking to simplify their operations and achieve greater success.\n\nMeet Our Team:\nTejas Deshmukh\nAsma Rajguru\nPriyanka Barman\nSakshi Kadam\n\nThank you for choosing Retail Pro. We look forward to partnering with you on your journey to success in the retail industry!",
                               font=("Arial", 12), wraplength=580, justify="left", bg="#d1e8e7", fg="#333333")
    about_paragraph.pack(padx=20, pady=(0, 20))

    # Back Button
    back_button = tk.Button(about_window, text="Back", font=("Arial", 12), command=lambda: close_about(about_window))
    back_button.place(x=1050, y=20, width=80, height=25)

    about_window.mainloop()

# Call the about_us function directly to open the About Us window
about_us()
