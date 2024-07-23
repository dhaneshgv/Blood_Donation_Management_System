import tkinter as tk
from UI.form.form_validation.runtime_validation import *
from UI.form.form_validation.complete_validation import *

def admin_login_display():
    admin_login_root = tk.Tk()
    admin_login_root.geometry("300x300")
    admin_login_root.title("Admin Login")
    admin_login_root.iconbitmap("assets/blood-donation.ico")


    # Defining the first row
    admin_id = tk.Label(admin_login_root, text ="Enter Admin ID", )
    admin_id.place(x = 50, y = 20)

    admin_id_entry = tk.Entry(admin_login_root, width = 35)
    admin_id_entry.place(x = 150, y = 20, width = 100)

    isdigit_ensure_validate = (admin_login_root.register(digit_ensure), "%P")

    admin_id_entry.configure(validate="key", validatecommand=isdigit_ensure_validate)


    password = tk.Label(admin_login_root, text ="Enter Password")
    password.place(x = 50, y = 50)

    password_entry = tk.Entry(admin_login_root, width = 35)
    password_entry.place(x = 150, y = 50, width = 100)

    atmost_thirty_char_ensure_validate = (admin_login_root.register(atmost_thirty_char_ensure), "%P")
    password_entry.configure(show="*",validate="key", validatecommand=atmost_thirty_char_ensure_validate)

    submitbtn = tk.Button(admin_login_root, text ="Login", command = lambda: admin_login_validator(admin_login_root,admin_id_entry.get(), password_entry.get()) )
    submitbtn.place(x = 150, y = 135, width = 55)

    admin_login_root.mainloop()

