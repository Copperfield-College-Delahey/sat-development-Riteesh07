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
userInfo = {}
selectedSlots = set()
registeredUsers = {}


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
def signIn():
    email = userEmail.get()
    password = userPassword.get()
    if not email or not password:
        messagebox.showerror("Error", "Please enter email and password.")
    elif "@gmail.com" not in email:
        messagebox.showerror("Invalid Email", "Only @ Gmail addresses are accepted.")
    elif email not in registeredUsers:
        messagebox.showerror("Account Not Found", "This email is not registered. Please sign up first.")
    elif registeredUsers[email]["password"] != password:
        messagebox.showerror("Wrong Password", "The password entered is incorrect.")
    else:
        name = registeredUsers[email]["name"]
        messagebox.showinfo("Signed In", f"Welcome back, {name}!")


def signUp():
    name = userName.get()
    email = userEmail.get()
    password = userPassword.get()

    if not name or not email or not password:
        messagebox.showerror("Error", "Please fill in the fields.")
    elif "@gmail.com" not in email:
        messagebox.showerror("Invalid Email", "Only Gmail addresses are accepted.")
    elif email in registeredUsers:
        messagebox.showwarning("Already Registered", "This email is already signed up.")
    else:
        registeredUsers[email] = {"name": name, "password": password}
        messagebox.showinfo("Signed Up", f"Account created, {name}!")
    

def showBookingAvailabilities():
    showFrame(bookCourtFrame)

def cancelSelectedBooking():
    messagebox.showinfo("Cancelled", "Booking has been cancelled.")


#button frames 
buttonFrame = ctk.CTkFrame(signInFrame, fg_color="transparent")
buttonFrame.grid(row=2, column=0, pady=5)

signInButton = ctk.CTkButton(buttonFrame, font=("Arial", 16), text="Sign In", width=200, height=45, fg_color="black", command=signIn)
signInButton.grid(row=0, column=0, padx=20, pady=10)

signUpButton = ctk.CTkButton(buttonFrame, font=("Arial", 16), text="Sign Up", width=200, height=45, fg_color="black", command=signUp)
signUpButton.grid(row=0, column=1, padx=20, pady=10)


#Booking Box
ctk.CTkLabel(signInFrame, text="Your Bookings:", font=ctk.CTkFont(size=16, underline=True)).grid(row=3, column=0, pady=(20, 0))

bookingDisplay = ctk.CTkTextbox(signInFrame, width=600, height=200, fg_color="light blue", text_color="black")
bookingDisplay.grid(row=4, column=0, pady=10)
bookingDisplay.configure(state="disabled") #ai
bookingDisplay.insert("0.0", "Date: 25/07/2025 | Court: 1 | Time: 6:00 PM – 7:00 PM")


#Booking tab
bookCourtFrame.grid_columnconfigure(0, weight=1)
ctk.CTkLabel(bookCourtFrame, text="Book Court Page", font=("Arial", 24)).grid(row=0, column=0, pady=50)


#Green red button

actionFrame = ctk.CTkFrame(signInFrame, fg_color="transparent")
actionFrame.grid(row=4, column=0, pady=(120,5), sticky="nsew")

actionFrame.grid_columnconfigure((0, 1), weight=1)  # Make columns expand

showButton = ctk.CTkButton( actionFrame, text="Show Booking Availabilities", fg_color="#28a745",hover_color="#218838", text_color="white", width=250, height=50,  font=("Arial", 16, "bold"), command=showBookingAvailabilities)
showButton.grid(row=0, column=0, padx=20, pady=10, sticky="e")

cancelButton = ctk.CTkButton(actionFrame,text="Cancel Selected Bookings",fg_color="#dc3545",hover_color="#c82333",text_color="white",width=250,height=50,font=("Arial", 16, "bold"))
cancelButton.grid(row=0, column=1, padx=20, pady=10, sticky="w")

#the initaial page 
showFrame(signInFrame)  #ai


#Booking Page

courtCount = 8
slotCount = 6
timeSlots = ["9-10", "10-11", "11-12", "12-13", "13-14", "14-15"]
pricePerSlot = 27

slotButtons = {}
bookedSlots = set()
selectedSlots = set()

#AI TO MAKE IT CENTRED
gridWrapper = ctk.CTkFrame(bookCourtFrame, fg_color="transparent")
gridWrapper.grid(row=1, column=0, pady=20)
gridWrapper.grid_columnconfigure(tuple(range(slotCount + 1)), weight=1)

#Time slots
ctk.CTkLabel(gridWrapper, text="Pick Date and Time", fg_color="yellow", width=100).grid(row=0, column=0, padx=1, pady=1)
for i in range(slotCount):
    ctk.CTkLabel(gridWrapper, text=timeSlots[i], fg_color="lightblue", width=100).grid(row=0, column=i+1, padx=1, pady=1)

bookingButtons = []  # to store all buttons if needed later

#confirm button
def updateTotalPrice():
    total = len(selectedSlots)* pricePerSlot
    totalLabel.configure(text=f"Total: ${total}")
    if total > 0:
        totalLabel.grid(row=2, column = 0, sticky= "w", padx=10)
        confirmButton.grid(row=2, column=0, sticky="e", padx=10)
    else:
        totalLabel.grid_remove()
        confirmButton.grid_remove()

#Slot colours
def toggleSlot(court, slot):
    key = (court,slot)
    btn = slotButtons[key]
    if key in bookedSlots:
        return

    if key in selectedSlots:
        selectedSlots.remove(key)
        btn.configure(fg_color="green")
    else:
        selectedSlots.add(key)
        btn.configure(fg_color="yellow")
    updateTotalPrice()

#Generate court and slot times AI
for court in range(courtCount):
    ctk.CTkLabel(gridWrapper, text=f"Court {court + 1}", fg_color="lightblue", width=100).grid(row=court + 1, column=0, padx=1, pady=1)

    rowButtons = []
    for slot in range(slotCount):
        btn = ctk.CTkButton(gridWrapper, text="", fg_color="green", width=100, height=40)
        btn.grid(row=court + 1, column=slot + 1, padx=1, pady=1)
        btn.configure(command=lambda c=court, s=slot: toggleSlot(c, s))
        rowButtons.append(btn)

    bookingButtons.append(rowButtons)
    slotButtons.update({(court, slot): btn for slot, btn in enumerate(rowButtons)})

#the confirm button (HALF AI)
bottomActionFrame = ctk.CTkFrame(bookCourtFrame)
bottomActionFrame.grid(row=2, column=0, pady=10, sticky="ew")
bottomActionFrame.grid_columnconfigure((0, 1), weight=1)


def confirmBooking():
    total = len(selectedSlots) * pricePerSlot
    paymentLabel.configure(
        text=f"Total Cost: ${total}\nPayment on site.\nClick OK to confirm your booking and receive an email"
    )
    showFrame(paymentFrame)


totalLabel = ctk.CTkLabel(bottomActionFrame, text="Total: $0", font=("Arial", 16))
confirmButton = ctk.CTkButton(bottomActionFrame, text="Confirm Booking", font=("Arial", 16), fg_color="blue", width=180, command=confirmBooking)
totalLabel.grid_remove()
confirmButton.grid_remove()


#Payment tab
paymentLabel = ctk.CTkLabel(paymentFrame, text="", font=("Arial", 16), wraplength=400, justify="center")
paymentLabel.pack(pady=30)

def paymentOK():
    messagebox.showinfo("Email Sent", "Your booking has been confirmed and an email has been sent.")
    showFrame(signInFrame)

okButton = ctk.CTkButton(paymentFrame, text="OK", fg_color="grey", command=paymentOK)
okButton.pack(pady=20)



app.mainloop()