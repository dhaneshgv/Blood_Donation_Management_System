import tkinter as tk
from UI.form.registration.donor_reg import donor_form_display
from UI.form.login.donor_login import donor_login_display

def enter_donor_form(root):
    root.destroy()
    donor_form_display()

def enter_donor_login(root):
    root.destroy()
    donor_login_display()

def donor_auth_display():
    # Create a new Tkinter window
    root = tk.Tk()

    # Set the window title
    root.title("Donor Authentication")

    # Set the window size
    root.geometry("400x200")

    # Set the window background color
    root.config(bg="#f2f2f2")

    # Create a label for the title
    title_label = tk.Label(root, text="Choose from below options", font=("Arial", 16), bg="#f2f2f2", fg="#333")
    title_label.pack(pady=10)

    # Create a frame for the buttons
    button_frame = tk.Frame(root, bg="#f2f2f2")
    button_frame.pack(pady=10)

    # Create a button for new registration
    new_reg_button = tk.Button(button_frame, text="Register", font=("Arial", 12), width=15, height=2, 
                               bg="#333", fg="#fff", activebackground="#555", activeforeground="#fff",
                               command=lambda: enter_donor_form(root) )
    new_reg_button.pack(side=tk.LEFT, padx=10)

    # Create a button for registered donor
    reg_donor_button = tk.Button(button_frame, text="Sign In", font=("Arial", 12), width=15, height=2, 
                                 bg="#333", fg="#fff", activebackground="#555", activeforeground="#fff",
                                 command=lambda: enter_donor_login(root)  )
    reg_donor_button.pack(side=tk.LEFT, padx=10)

    # Start the Tkinter event loop
    root.mainloop()