import customtkinter as ctk 
from tkinter import messagebox

#app
app = ctk.CTk()
app.title("Badminton Booking System") 
app.geometry ("800x600")

#Frame
topFrame = ctk.CTkFrame(app)
topFrame.pack(pady=50)

#TITLE
titleLabel = ctk.CTkLabel(topFrame, text="Booking System", font=("Arial", 28))
titleLabel.grid(row=0, column=0,)

#NConfigure app
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight= 1)
app.grid_rowconfigure(1, weight= 4)
app.grid_rowconfigure(2, weight= 1)

#button
signIn = ctk.CTkFrame(topFrame)
signIn.grid(row=1, column= 0 , sticky="e", padx=15, pady=15)

app.mainloop()