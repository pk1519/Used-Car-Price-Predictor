import tkinter as tk
from tkinter import messagebox


def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if the username and password are correct
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# Create the main window
root = tk.Tk()
root.title("Login Page")

# Create and place labels and entry fields for username and password
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=5)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

# Create and place the login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()
