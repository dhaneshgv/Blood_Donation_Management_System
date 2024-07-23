import tkinter as tk
from UI.donor_auth import donor_auth_display
from UI.form.login.hospital_login import hospital_login_display
from UI.form.login.admin_login import admin_login_display

# Create the main window
root = tk.Tk()
root.iconbitmap("./assets/blood-donation.ico")

# Set the window title
root.title("Welcome Page")

def enter_donor():
    root.destroy()
    donor_auth_display()

def enter_hospital():
    root.destroy()
    hospital_login_display()

def enter_admin():

    root.destroy()
    admin_login_display()

def show_frame(frame):
    frame.tkraise()

def welcome_screen_display():

    # Create a canvas widget to hold the background image
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.grid(row=0, column=0, sticky="nsew")

    # Load the background image
    background_image = tk.PhotoImage(file="assets/welcome_image.png")

    # Set the background image
    canvas.create_image(0, 0, anchor="nw", image=background_image)

    # Create a label widget with a welcome message
    label = tk.Label(canvas, text="BLOOD DONATION MANAGEMENT SYSTEM", font=("Helvetica", 30), bg="white",padx=4)
    label.place(relx=0.55, rely=0.03, anchor="n")

    # Create a frame to hold the buttons
    button_frame = tk.Frame(canvas)
    button_frame.place(relx=0.5, rely=0.6, anchor="center")

    # Create the buttons within the frame
    donor = tk.Button(button_frame, text="DONOR", command=enter_donor, bg="orange", width=10, height=2)
    donor.grid(row=0, column=0, padx=10, pady=10)

    hospital = tk.Button(button_frame, text="HOSPITAL", command=enter_hospital, bg="green",width=10, height=2)
    hospital.grid(row=0, column=1,padx=10, pady=10)

    admin = tk.Button(button_frame, text="ADMIN", command=enter_admin, bg="violet",width=10, height=2)
    admin.grid(row=0, column=2,padx=10,pady=10)

    root.mainloop()