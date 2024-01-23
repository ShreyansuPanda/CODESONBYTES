#CodeOnBytes Task-3:Develop a secure password manager and organizes password
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_password(key, password):
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def decrypt_password(key, encrypted_password):
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()

passwords = {}

def add_password():
    service = service_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if service and username and password:
        encrypted_password = encrypt_password(key, password)
        passwords[service] = {'username': username, 'password': encrypted_password}
        messagebox.showinfo("Success", "Password added successfully!")
    else:
        messagebox.showwarning("Error", "Please fill in all the fields.")

def copy_to_clipboard(data):
    root.clipboard_clear()
    root.clipboard_append(data)
    root.update()

def get_password():
    service = service_entry.get()
    if service in passwords:
        encrypted_password = passwords[service]['password']
        decrypted_password = decrypt_password(key, encrypted_password)
        confirmation = messagebox.askyesno("Copy to Clipboard", "Do you want to copy the password to the clipboard?")
        if confirmation:
            copy_to_clipboard(decrypted_password)
        messagebox.showinfo("Password", f"Username: {passwords[service]['username']}\nPassword: {decrypted_password}")
    else:
        messagebox.showwarning("Error", "Password not found.")

def show_all_accounts():
    if passwords:
        accounts_info = "\n".join([f"{service}: {passwords[service]['username']}" for service in passwords])
        messagebox.showinfo("All Accounts", accounts_info)
    else:
        messagebox.showinfo("All Accounts", "No accounts available.")

def delete_account():
    service = service_entry.get()
    if service in passwords:
        confirmation = messagebox.askyesno("Confirmation", f"Do you really want to delete the account '{service}'?")
        if confirmation:
            del passwords[service]
            messagebox.showinfo("Success", f"Account '{service}' deleted successfully!")
    else:
        messagebox.showwarning("Error", "Account not found.")

key = generate_key()

instructions = '''Add Password: Fill in all the fields and press "Add Password"\n
View Password: Enter the Account Name and press "Get Password"\n
Show Accounts: Press "Show All Accounts"\n
Delete Account: Enter the Account Name and press "Delete Account".'''


root = tk.Tk()
root.title("Password Manager")
root.configure(bg="#F7DC6F")

root.resizable(False, False)

center_frame = tk.Frame(root, bg="#F2FEDC")
center_frame.grid(row=0, column=0, padx=20, pady=22)

instruction_label = tk.Label(center_frame, text=instructions,font=('Helvetica', 10, 'bold'), bg="#F2FEDC")
instruction_label.grid(row=0, column=1, padx=10, pady=6)

service_label = tk.Label(center_frame, text="Account:",font=('Helvetica', 10, 'bold'), bg="#F2FEDC")
service_label.grid(row=1, column=0, padx=10, pady=5)
service_entry = tk.Entry(center_frame,width=60)
service_entry.grid(row=1, column=1, padx=10, pady=5)

username_label = tk.Label(center_frame, text="Username:",font=('Helvetica', 10, 'bold'), bg="#F2FEDC")
username_label.grid(row=2, column=0, padx=10, pady=5)
username_entry = tk.Entry(center_frame,width=60)
username_entry.grid(row=2, column=1, padx=10, pady=5)

password_label = tk.Label(center_frame, text="Password:",font=('Helvetica', 10, 'bold'), bg="#F2FEDC")
password_label.grid(row=3, column=0, padx=15, pady=10)
password_entry = tk.Entry(center_frame, show="*",width=60)
password_entry.grid(row=3, column=1, padx=15, pady=10)

add_button = tk.Button(center_frame, text="Add Password", command=add_password, height=1, width=15)
add_button.grid(row=5, column=0, padx=15, pady=10)

get_button = tk.Button(center_frame, text="Get Password", command=get_password, height=1, width=15)
get_button.grid(row=5, column=1, padx=15, pady=10)

show_all_button = tk.Button(center_frame, text="Show All Accounts", command=show_all_accounts, height=1, width=15)
show_all_button.grid(row=6, column=0, padx=15, pady=10)

delete_button = tk.Button(center_frame, text="Delete Account", command=delete_account, height=1, width=15)
delete_button.grid(row=6, column=1, padx=15, pady=10)

root.mainloop()
