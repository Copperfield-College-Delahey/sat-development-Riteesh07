import customtkinter as ctk 
from tkinter import messagebox
from datetime import datetime #AI

# App setup
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

#app
app = ctk.CTk()
app.title("Badminton Booking System") 
app.geometry ("1100x700")

app.grid_columnconfigure(0, weight=1)

#Navigation stuff
topNavFrame = ctk.CTkFrame(app, fg_color="grey", height=50)
topNavFrame.grid(row=0, column=0, sticky="ew")

navFont = ctk.CTkFont(family="Arial", size=14, weight="bold")

signInTabButton = ctk.CTkButton(topNavFrame, text="Sign In", font=navFont, width=100, command=lambda: showFrame(signInFrame))
signInTabButton.grid(row=0, column=0, padx=10, pady=10)

bookCourtTabButton = ctk.CTkButton(topNavFrame, text="Book Court", font=navFont, width=100, command=lambda: showFrame(bookCourtFrame))
bookCourtTabButton.grid(row=0, column=1, padx=10)

paymentTabButton = ctk.CTkButton(topNavFrame, text="Payment", font=navFont, width=100, command=lambda: showFrame(paymentFrame))
paymentTabButton.grid(row=0, column=2, padx=10)

#pages
signInFrame = ctk.CTkFrame(app)
bookCourtFrame = ctk.CTkFrame(app)
paymentFrame = ctk.CTkFrame(app)

for frame in (signInFrame, bookCourtFrame, paymentFrame):  #AI
    frame.grid(row=1, column=0, sticky="nsew")

def showFrame(frame):   #ai
    frame.tkraise()

#list
bookings = {}
user_info = {}
selected_slots = []
registered_users = {}


#Sign in page

signInFrame.grid_columnconfigure(0, weight=1)
signInFrame.grid_rowconfigure(1, weight=2)   
signInFrame.grid_rowconfigure(2, weight=1)  
signInFrame.grid_rowconfigure(3, weight=1)   
signInFrame.grid_rowconfigure(4, weight=1)  
signInFrame.grid_rowconfigure(5, weight=1)   

inputFrame = ctk.CTkFrame(signInFrame, fg_color="light blue")
inputFrame.grid(row=1, column=0, pady=10, padx=40, sticky="nsew")
inputFrame.grid_columnconfigure(0, weight=1)

userNameLabel = ctk.CTkLabel(inputFrame, text="User Name:", font=("Arial", 18))
userNameLabel.grid(row=0, column=0, sticky="w", padx=30, pady=(20, 5))
userName = ctk.CTkEntry(inputFrame, width=400, height=40, font=("Arial", 14))
userName.grid(row=1, column=0, padx=30, pady=(0, 10))

userEmailLabel = ctk.CTkLabel(inputFrame, text="Email:", font=("Arial", 18))
userEmailLabel.grid(row=2, column=0, sticky="w", padx=30, pady=(10, 5))
userEmail = ctk.CTkEntry(inputFrame, width=400, height=40, font=("Arial", 14))
userEmail.grid(row=3, column=0, padx=30, pady=(0, 10))

userPasswordLabel = ctk.CTkLabel(inputFrame, text="Password:", font=("Arial", 18))
userPasswordLabel.grid(row=4, column=0, sticky="w", padx=30, pady=(10, 5))
userPassword = ctk.CTkEntry(inputFrame, width=400, height=40, font=("Arial", 14), show="*") #show was ai
userPassword.grid(row=5, column=0, padx=30, pady=(0, 20))

#functions
def sign_in():
    email = userEmail.get()
    password = userPassword.get()
    if not email or not password:
        messagebox.showerror("Error", "Please enter email and password.")
    elif "@gmail.com" not in email:
        messagebox.showerror("Invalid Email", "Only Gmail addresses are accepted.")
    elif email not in registered_users:
        messagebox.showerror("Account Not Found", "This email is not registered. Please sign up first.")
    elif registered_users[email]["password"] != password:
        messagebox.showerror("Wrong Password", "The password entered is incorrect.")
    else:
        name = registered_users[email]["name"]
        messagebox.showinfo("Signed In", f"Welcome back, {name}!")


def sign_up():
    name = userName.get()
    email = userEmail.get()
    password = userPassword.get()

    if not name or not email or not password:
        messagebox.showerror("Error", "Please fill in the fields.")
    elif "@gmail.com" not in email:
        messagebox.showerror("Invalid Email", "Only Gmail addresses are accepted.")
    elif email in registered_users:
        messagebox.showwarning("Already Registered", "This email is already signed up.")
    else:
        registered_users[email] = {"name": name, "password": password}
        messagebox.showinfo("Signed Up", f"Account created, {name}!")
    

def showBookingAvailabilities():
    messagebox.showinfo("Bookings")

def cancelSelectedBooking():
    messagebox.showinfo("Cancelled", "Booking has been cancelled.")


#button frames 
buttonFrame = ctk.CTkFrame(signInFrame, fg_color="transparent")
buttonFrame.grid(row=2, column=0, pady=5)

signInButton = ctk.CTkButton(buttonFrame, font=("Arial", 16), text="Sign In", width=200, height=45, fg_color="black", command=sign_in)
signInButton.grid(row=0, column=0, padx=20, pady=10)

signUpButton = ctk.CTkButton(buttonFrame, font=("Arial", 16), text="Sign Up", width=200, height=45, fg_color="black", command=sign_up)
signUpButton.grid(row=0, column=1, padx=20, pady=10)


#Booking Box
ctk.CTkLabel(signInFrame, text="Your Bookings:", font=ctk.CTkFont(size=16, underline=True)).grid(row=3, column=0, pady=(20, 0))

bookingDisplay = ctk.CTkTextbox(signInFrame, width=600, height=100, fg_color="light blue", text_color="black")
bookingDisplay.grid(row=4, column=0, pady=10)
bookingDisplay.configure(state="disabled") #ai
bookingDisplay.insert("0.0", "Date: 25/07/2025 | Court: 1 | Time: 6:00 PM – 7:00 PM")


#Booking tab
bookCourtFrame.grid_columnconfigure(0, weight=1)
ctk.CTkLabel(bookCourtFrame, text="Book Court Page", font=("Arial", 24)).grid(row=0, column=0, pady=50)


#Green red button
actionFrame = ctk.CTkFrame(signInFrame, fg_color="transparent")
actionFrame.grid(row=5, column=0, pady=10)

showButton = ctk.CTkButton(actionFrame, text="Show Booking Availabilities", fg_color="green", width=260)
showButton.grid(row=0, column=0, padx=20, pady=10)

cancelButton = ctk.CTkButton(actionFrame, text="Cancel Selected Bookings", fg_color="red", width=260)
cancelButton.grid(row=0, column=1, padx=20, pady=10)

#the initaial page 
showFrame(signInFrame)  #ai

app.mainloop()