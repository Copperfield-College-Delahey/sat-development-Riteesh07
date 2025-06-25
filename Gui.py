import customtkinter as ctk 
from tkinter import messagebox

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

#button frame
buttonFrame = ctk.CTkFrame(app, fg_color="grey")
buttonFrame.pack(pady=0)

signInButton = ctk.CTkButton(buttonFrame, font=("Bold",15), text="Sign In", fg_color="Black")
signInButton.pack(anchor="w", padx=20)

signUpButton = ctk.CTkButton(buttonFrame, font=("Bold",15), text="Sign Up", fg_color="Black")
signUpButton.pack(anchor="w", padx=20)


app.mainloop()