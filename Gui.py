import customtkinter as ctk 
from tkinter import messagebox

# App setup
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

#app
app = ctk.CTk()
app.title("Badminton Booking System") 
app.geometry ("1100x700")

#list
bookings = {}
user_info = {}
selected_slots = []

#Box Frame
inputFrame = ctk.CTkFrame(app, fg_color="lightblue")
inputFrame.pack(pady=5)

#username
userNameLabel = ctk.CTkLabel(inputFrame, text="User Name:")
userNameLabel.pack(anchor="w", padx=20)
userName = ctk.CTkEntry(inputFrame, width=300)
userName.pack(padx=20, pady=5)

#email
userEmailLabel = ctk.CTkLabel(inputFrame, text="Email:")
userEmailLabel.pack(anchor="w", padx=20)
userEmail = ctk.CTkEntry(inputFrame, width=300)
userEmail.pack(padx=20, pady=5)

#password
userPasswordLabel = ctk.CTkLabel(inputFrame, text="Password:")
userPasswordLabel.pack(anchor="w", padx=20)
userPassword = ctk.CTkEntry(inputFrame, width=300, show="*")
userPassword.pack(padx=20, pady=5)

#functions
def sign_in():
    name = userName.get()
    email = userEmail.get()
    password = userPassword.get()

    if not name or not email or not password:
        messagebox.showerror("Error", "Please fill in the fields.")
    else:
        messagebox.showinfo("Signed In", f"Welcome, {name}!")



def sign_up():
    name = userName.get()
    email = userEmail.get()
    password = userPassword.get()

    if not name or not email or not password:
        messagebox.showerror("Error", "Please fill in the fields")
    else:
        messagebox.showinfo("Signed Up", f"acoount is created, {name}!")

def showBookingAvailabilities():
    messagebox.showinfo("Bookings")

def cancelSelectedBooking():
    messagebox.showinfo("Cancelled", "Booking has been cancelled.")


#button frames 
buttonFrame = ctk.CTkFrame(app, fg_color="black")
buttonFrame.pack(pady=0)

signInButton = ctk.CTkButton(buttonFrame, font=("Bold",15), text="Sign In", fg_color="Black")
signInButton.pack(anchor="w", padx=20)

signUpButton = ctk.CTkButton(buttonFrame, font=("Bold",15), text="Sign Up", fg_color="Black")
signUpButton.pack(anchor="w", padx=20)


#Booking Box
ctk.CTkLabel(app, text="Your Bookings:", font=ctk.CTkFont(size=15, underline=True)).pack(pady=(20, 0))

bookingDisplay = ctk.CTkTextbox(app, width=600, height=100, fg_color="light blue", text_color="white")
bookingDisplay.insert("0.0", "Date: 25/07/2025 | Court: 1 | Time: 6:00 PM – 7:00 PM")
bookingDisplay.configure(state="disabled") #ai
bookingDisplay.pack(pady=10)

#Green red button
actionFrame = ctk.CTkFrame(app, fg_color="transparent")
actionFrame.pack(pady=10)

showButton = ctk.CTkButton(actionFrame, text="Show Booking Availabilities", fg_color="green", command=showBookingAvailabilities, width=260)
showButton.pack(pady=5)

cancelButton = ctk.CTkButton(actionFrame, text="Cancel Selected Bookings", fg_color="red", command=cancelSelectedBooking, width=260)
cancelButton.pack(pady=5)

app.mainloop()