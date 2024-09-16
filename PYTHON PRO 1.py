import tkinter as tk
from tkinter import messagebox
import re

# Function to check password strength
def check_password_strength():
    password = entry.get()
    
    # Basic criteria checks
    length = len(password) >= 8
    digit = re.search(r"\d", password) is not None
    upper = re.search(r"[A-Z]", password) is not None
    lower = re.search(r"[a-z]", password) is not None
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Calculate password strength
    if length and digit and upper and lower and special:
        result.set("Strong Password 💪")
    elif length and (digit or upper or lower or special):
        result.set("Moderate Password 🔐")
    else:
        result.set("Weak Password 🚨")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")

# Input field
tk.Label(root, text="Enter your password:").pack(pady=10)
entry = tk.Entry(root, show='*', width=30)
entry.pack(pady=5)

# Button to check strength
tk.Button(root, text="Check Strength", command=check_password_strength).pack(pady=10)

# Display result
result = tk.StringVar()
tk.Label(root, textvariable=result, font=('Helvetica', 12)).pack(pady=5)

# Run the GUI loop
root.mainloop()
