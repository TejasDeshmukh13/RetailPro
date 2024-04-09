from tkinter import *
from tkinter import messagebox
import mysql.connector


class UserProfile:
	def __init__(self, root, user_id):
		self.root = root
		self.root.title("User Profile")
		self.root.geometry("600x400")  # Increase frame size

		try:
			# Connect to MySQL database
			self.db = mysql.connector.connect(
				host="localhost",
				user="root",
				password="D@zypiyu123",
				database="retailers",
				port=3306
			)

			# Fetch user data from the database
			self.cursor = self.db.cursor()
			query = "SELECT * FROM login WHERE username = %s"
			self.cursor.execute(query, (user_id,))
			user_data = self.cursor.fetchone()

			# Display user profile information
			if user_data:
				self.display_profile(user_data)
			else:
				messagebox.showerror("Error", "User not found")
				self.root.destroy()
		except mysql.connector.Error as err:
			messagebox.showerror("MySQL Error", f"Error: {err}")
			self.root.destroy()

	def display_profile(self, user_data):
		# User profile frame
		frame = Frame(self.root)
		frame.pack(pady=20)  # Add some padding

		# Load and display image
		img = PhotoImage(file='hyy.png')
		img_label = Label(frame, image=img)
		img_label.image = img  # Keep a reference to the image to prevent garbage collection
		img_label.pack()

		# User profile labels with larger font
		Label(frame, text="User Profile", font=("Helvetica", 24, "bold")).pack(pady=10)  # Larger font
		Label(frame, text=f"Username: {user_data[1]}", font=("Helvetica", 16)).pack()  # Larger font
		Label(frame, text=f"Email: {user_data[2]}", font=("Helvetica", 16)).pack()  # Larger font
		Label(frame, text=f"Mobile: {user_data[3]}", font=("Helvetica", 16)).pack()  # Larger font


def main():
	root = Tk()
	user_id = 1  # Replace with the actual user ID
	UserProfile(root, user_id)
	root.mainloop()


if __name__ == "__main__":
	main()
