import customtkinter as ctk 
from tkinter import messagebox
from datetime import datetime #AI
import json
from pathlib import Path

DATA_FILE = Path("badminton_data.json")

# App setup
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

#app
app = ctk.CTk()
app.title("Badminton Booking System") 
app.geometry ("1100x700")
isLoggedIn = False

app.grid_columnconfigure(0, weight=1)

#Navigation stuff
topNavFrame = ctk.CTkFrame(app, fg_color="grey", height=50)
topNavFrame.grid(row=0, column=0, sticky="ew")

navFont = ctk.CTkFont(family="Arial", size=14, weight="bold")

signInTabButton = ctk.CTkButton(topNavFrame, text="Sign In", font=navFont, width=100, command=lambda: showFrame(signInFrame))
signInTabButton.grid(row=0, column=0, padx=10, pady=10)


#pages
signInFrame = ctk.CTkFrame(app)
bookCourtFrame = ctk.CTkFrame(app)
paymentFrame = ctk.CTkFrame(app)

for frame in (signInFrame, bookCourtFrame, paymentFrame):  #AI
    frame.grid(row=1, column=0, sticky="nsew")

def showFrame(frame):   #ai
    frame.tkraise()

#Dictionary
bookings = {}
userInfo = {}
selectedSlots = set()
registeredUsers = {}
userBookings = {}     
bookedSlots = {}       
currentUserEmail = None

pendingSelections = set()
pendingDate = None

def load_data(): #half ai
    global registeredUsers, userBookings, bookedSlots
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            registeredUsers = data.get("registeredUsers", {})
            userBookings = data.get("userBookings", {})
            raw_booked = data.get("bookedSlots", {})
            bookedSlots = {
                date: set(map(tuple, slots_list))
                for date, slots_list in raw_booked.items()
            }
        except Exception as e:
            messagebox.showwarning("Load Error", f"Could not load data: {e}")
            registeredUsers = {}
            userBookings = {}
            bookedSlots = {}
    else:
        registeredUsers = {}
        userBookings = {}
        bookedSlots = {}

def save_data(): #ai
    try:
        serializable_booked = {
            date: [list(pair) for pair in slots_set]
            for date, slots_set in bookedSlots.items()
        }
        data = {
            "registeredUsers": registeredUsers,
            "userBookings": userBookings,
            "bookedSlots": serializable_booked,
        }
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        messagebox.showwarning("Save Error", f"Could not save data: {e}")

load_data()

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
    global isLoggedIn, currentUserEmail #AI
    name = userName.get().strip()
    email = userEmail.get().strip().lower()
    password = userPassword.get().strip()

    if name and email and password:
        if email in registeredUsers and registeredUsers[email]["password"] == password:
            isLoggedIn = True
            currentUserEmail = email
            messagebox.showinfo("Login Successful", f"Welcome back, {registeredUsers[email]['name']}!")
            displayBookings() #ai
            showFrame(bookCourtFrame)
        else:
            messagebox.showerror("Login Failed", "Invalid email or password.")
    else:
        messagebox.showwarning("Sign In Failed", "Please fill in all fields.")

def goToBookCourt():
    if not isLoggedIn:
        messagebox.showerror("Access Denied", "You must sign in before booking a court.")
        return
    showFrame(bookCourtFrame)

def goToPaymentTab():
    if not isLoggedIn:
        messagebox.showerror("Access Denied", "You must sign in before accessing the payment tab.")
        return
    showFrame(paymentFrame)

def signUp():
    name = userName.get().strip()
    email = userEmail.get().strip().lower()
    password = userPassword.get().strip()

    if not name or not email or not password:
        messagebox.showerror("Error", "Please fill in the fields.")
    elif "@gmail.com" not in email:
        messagebox.showerror("Invalid Email", "Only Gmail addresses are accepted.")
    elif email in registeredUsers:
        messagebox.showwarning("Already Registered", "This email is already signed up.")
    else:
        registeredUsers[email] = {"name": name, "password": password}
        messagebox.showinfo("Signed Up", f"Account created, {name}!")
        save_data()

bookCourtTabButton = ctk.CTkButton(topNavFrame, text="Book Court", font=navFont, width=100, command=goToBookCourt)
bookCourtTabButton.grid(row=0, column=1, padx=10)

paymentTabButton = ctk.CTkButton(topNavFrame, text="Payment", font=navFont, width=100, command=goToPaymentTab)
paymentTabButton.grid(row=0, column=2, padx=10)

def showBookingAvailabilities():
    if not isLoggedIn:
        messagebox.showerror("Access Denied", "You must sign in before booking a court.")
        return
    showFrame(bookCourtFrame)

def cancelSelectedBooking():
    global bookedSlots, userBookings, currentUserEmail
    if not isLoggedIn or currentUserEmail not in userBookings:
        messagebox.showerror("Not Signed In", "Please sign in first.")
        return
    if not cancelSelection:
        messagebox.showinfo("Nothing Selected", "Select bookings first, then click Cancel.")
        return

    bookings_for_user = userBookings[currentUserEmail]
    to_cancel = sorted(cancelSelection, reverse=True)
    cancelled_msgs = []

    for idx in to_cancel:
        if idx < 0 or idx >= len(bookings_for_user):
            continue
        rec = bookings_for_user[idx]
        date_str = rec["date"]
        court = rec["court"]
        slot = rec["slot"]

        if date_str in bookedSlots:
            bookedSlots[date_str].discard((court, slot))
            if not bookedSlots[date_str]:
                del bookedSlots[date_str]

        bookings_for_user.pop(idx)
        cancelled_msgs.append(f"{date_str} | Court {court+1} | {timeSlots[slot]}")

    userBookings[currentUserEmail] = bookings_for_user
    cancelSelection.clear()
    displayBookings()
    updateSlotColors()
    save_data()

    if cancelled_msgs:
        messagebox.showinfo("Cancelled", "Cancelled booking(s):\n" + "\n".join(cancelled_msgs))


#button frames 
buttonFrame = ctk.CTkFrame(signInFrame, fg_color="transparent")
buttonFrame.grid(row=2, column=0, pady=5)

signInButton = ctk.CTkButton(buttonFrame, font=("Arial", 16), text="Sign In", width=200, height=45, fg_color="black", command=signIn)
signInButton.grid(row=0, column=0, padx=20, pady=10)

signUpButton = ctk.CTkButton(buttonFrame, font=("Arial", 16), text="Sign Up", width=200, height=45, fg_color="black", command=signUp)
signUpButton.grid(row=0, column=1, padx=20, pady=10)

#Booking Box
ctk.CTkLabel(signInFrame, text="Your Bookings:", font=ctk.CTkFont(size=16, underline=True)).grid(row=3, column=0, pady=(20, 0))

bookingListFrame = ctk.CTkScrollableFrame(signInFrame, width=600, height=200)
bookingListFrame.grid(row=4, column=0, pady=10, sticky="ew")

bookingRowButtons = {} 
cancelSelection = set()

def toggleCancelSelection(i):
    if i in cancelSelection:
        cancelSelection.remove(i)
    else:
        cancelSelection.add(i)
    updateBookingButtons()

def updateBookingButtons():
    for idx, btn in bookingRowButtons.items():
        if idx in cancelSelection:
            btn.configure(fg_color="#ffb74d", hover_color="#fb8c00")
        else:
            btn.configure(fg_color="light blue", hover_color="#cce6ff")

def displayBookings():
    # Clear existing
    for w in bookingListFrame.winfo_children():
        w.destroy()
    bookingRowButtons.clear()
    cancelSelection.clear()

    if not isLoggedIn or currentUserEmail not in userBookings or len(userBookings[currentUserEmail]) == 0:
        lbl = ctk.CTkLabel(bookingListFrame, text="No bookings yet.")
        lbl.pack(pady=6)
        return

    bookings_for_user = userBookings[currentUserEmail]
    for idx, rec in enumerate(bookings_for_user):
        date_str = rec["date"]
        court = rec["court"]
        slot = rec["slot"]
        time_str = timeSlots[slot]
        text = f"{date_str}  |  Court {court + 1}  |  {time_str}"
        btn = ctk.CTkButton(
            bookingListFrame,
            text=text,
            fg_color="light blue",
            text_color="black",
            hover_color="#cce6ff",
            command=lambda i=idx: toggleCancelSelection(i)
        )
        btn.pack(fill="x", padx=6, pady=4)
        bookingRowButtons[idx] = btn

#Booking tab
bookCourtFrame.grid_columnconfigure(0, weight=1)
ctk.CTkLabel(bookCourtFrame, text="Book Court Page", font=("Arial", 24)).grid(row=0, column=0, pady=50)


#Green red button

actionFrame = ctk.CTkFrame(signInFrame, fg_color="transparent")
actionFrame.grid(row=4, column=0, pady=(120,5), sticky="nsew")

actionFrame.grid_columnconfigure((0, 1), weight=1)  # Make columns expand

showButton = ctk.CTkButton( actionFrame, text="Show Booking Availabilities", fg_color="#28a745",hover_color="#218838", text_color="white", width=250, height=50,  font=("Arial", 16, "bold"), command=showBookingAvailabilities)
showButton.grid(row=0, column=0, padx=20, pady=10, sticky="e")

cancelButton2 = ctk.CTkButton(actionFrame,text="Cancel Selected Bookings",fg_color="#dc3545",hover_color="#c82333",text_color="white",width=250,height=50,font=("Arial", 16, "bold"), command=cancelSelectedBooking)
cancelButton2.grid(row=0, column=1, padx=20, pady=10, sticky="w")

#the initaial page 
showFrame(signInFrame)  #ai


#Booking Page

courtCount = 8
slotCount = 6
timeSlots = ["9-10", "10-11", "11-12", "12-13", "13-14", "14-15"]
pricePerSlot = 27

#AI TO MAKE IT CENTRED
gridWrapper = ctk.CTkFrame(bookCourtFrame, fg_color="transparent")
gridWrapper.grid(row=1, column=0, pady=20)
gridWrapper.grid_columnconfigure(tuple(range(slotCount + 1)), weight=1)

#Time slots
selectedDate = None
dateFrame = ctk.CTkFrame(bookCourtFrame, fg_color="transparent")
dateFrame.grid(row=0, column=0, sticky="w", padx=20, pady=(10, 0))  

ctk.CTkLabel(dateFrame, text="Enter Date (DD/MM):", width=160).grid(row=0, column=0, padx=5, pady=5)
dateEntry = ctk.CTkEntry(dateFrame, width=100)
dateEntry.grid(row=0, column=1, padx=5, pady=5)

def updateSlotColors(): #half ai
    if selectedDate is None:
        for btn in slotButtons.values():
            btn.configure(fg_color="grey", state="disabled", text="")
        return

    bookedForDate = bookedSlots.get(selectedDate, set())

    for court in range(courtCount):
        for slot in range(slotCount):
            key = (court, slot)
            btn = slotButtons[key]
            if key in bookedForDate:
                btn.configure(fg_color="red", text="Booked", state="disabled")
            else:
                if key in selectedSlots:
                    btn.configure(fg_color="yellow", text="", state="normal")
                else:
                    btn.configure(fg_color="green", text="", state="normal")

#confirms the date 
def validateDate():
    global selectedDate, selectedSlots
    date_text = dateEntry.get()
    try:
        full_date = f"{date_text}/2025"
        datetime.strptime(full_date, "%d/%m/%Y")
        selectedDate = full_date
        selectedSlots.clear()   
        messagebox.showinfo("Date Selected", f"Date set to: {selectedDate}")
        updateSlotColors()
        updateTotalPrice()
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter date in DD/MM format.")

confirmDateBtn = ctk.CTkButton(dateFrame, text="Set Date", width=80, command=validateDate)
confirmDateBtn.grid(row=0, column=2, padx=5, pady=5)


for i in range(slotCount):
    ctk.CTkLabel(gridWrapper, text=timeSlots[i], fg_color="lightblue", width=100).grid(row=0, column=i+1, padx=1, pady=1)

bookingButtons = []  # to store all buttons if needed later
slotButtons = {}

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
    global selectedDate
    if selectedDate is None:
        messagebox.showerror("No Date Selected", "Please select a date first.")
        return

    key = (court, slot)
    btn = slotButtons[key]

    bookedForDate = bookedSlots.get(selectedDate, set())

    if key in bookedForDate:
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
        btn = ctk.CTkButton(gridWrapper, text="", fg_color="grey", width=100, height=40)
        btn.grid(row=court + 1, column=slot + 1, padx=1, pady=1)
        btn.configure(command=lambda c=court, s=slot: toggleSlot(c, s))
        rowButtons.append(btn)

    bookingButtons.append(rowButtons)
    slotButtons.update({(court, slot): btn for slot, btn in enumerate(rowButtons)})

totalLabel = ctk.CTkLabel(bookCourtFrame, text="", font=("Arial", 16, "bold"))
confirmButton = ctk.CTkButton(bookCourtFrame, text="Confirm Booking", font=("Arial", 16, "bold"), fg_color="#007bff", hover_color="#0056b3", text_color="white")

def confirmBooking(): #half ai
    """Do NOT finalize booking here. Just show Payment tab with the total."""
    global pendingSelections, pendingDate
    if not isLoggedIn or currentUserEmail is None:
        messagebox.showerror("Not Signed In", "Please sign in first.")
        return
    if selectedDate is None:
        messagebox.showerror("No Date Selected", "Please select a date.")
        return
    if not selectedSlots:
        messagebox.showerror("No Slots Selected", "Please select at least one slot to book.")
        return
    bookedForDate = bookedSlots.get(selectedDate, set())
    for pair in selectedSlots:
        if pair in bookedForDate:
            messagebox.showerror("Slot Taken", "One or more selected slots are already booked.")
            return
    pendingSelections = set(selectedSlots)
    pendingDate = selectedDate
    total = len(pendingSelections) * pricePerSlot
    paymentLabel.configure(
        text=f"Total Cost: ${total}\nPayment on site.\nClick OK to confirm your booking and receive an email"
    )
    showFrame(paymentFrame)

confirmButton.configure(command=confirmBooking)


#Payment page
paymentLabel = ctk.CTkLabel(paymentFrame, text="", font=("Arial", 16), wraplength=400, justify="center")
paymentLabel.pack(pady=30)

def paymentOK(): #half ai
    """Finalize the booking here when user clicks OK."""
    global bookedSlots, userBookings, pendingSelections, pendingDate, selectedSlots
    if not pendingSelections or pendingDate is None:
        showFrame(signInFrame)
        return

    if pendingDate not in bookedSlots:
        bookedSlots[pendingDate] = set()
    bookedSlots[pendingDate].update(pendingSelections)

    if currentUserEmail not in userBookings:
        userBookings[currentUserEmail] = []
    for court, slot in pendingSelections:
        userBookings[currentUserEmail].append({"date": pendingDate, "court": court, "slot": slot})
        if pendingDate == selectedDate and (court, slot) in slotButtons:
            btn = slotButtons[(court, slot)]
            btn.configure(fg_color="red", state="disabled", text="Booked")

    selectedSlots.clear()
    pendingSelections.clear()
    displayBookings()
    updateSlotColors()
    updateTotalPrice()
    save_data()

    messagebox.showinfo("Email Sent", "Your booking has been confirmed and an email has been sent.")
    showFrame(signInFrame)

okButton = ctk.CTkButton(paymentFrame, text="OK", fg_color="grey", command=paymentOK)
okButton.pack(pady=20)

showFrame(signInFrame)  # start at sign in page

app.mainloop()
