import tkinter as tk
from tkinter import ttk

def about_us():
    about_window = tk.Toplevel(root)
    about_window.title("About Us")
    about_window.geometry("600x400")
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

# Create main window
root = tk.Tk()
root.title("Retail Pro - About Us")
root.geometry("400x300")

# Set a custom style for buttons
style = ttk.Style()
style.configure("TButton", font=("Arial", 14), background="#4caf50", foreground="white", relief=tk.FLAT)

# About Us Button
about_button = ttk.Button(root, text="About Us", command=about_us)
about_button.pack(pady=50)

# Run the main event loop
root.mainloop()
