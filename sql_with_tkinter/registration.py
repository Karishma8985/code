import mysql.connector
from tkinter import *
from tkinter import messagebox


# Function to handle registration
def register():
    # Fetching values from the entries
    name = en1.get()
    email = en3.get()
    contact_number = en4.get()
    gender = vars.get()
    state = cv.get()
    password = en6.get()
    confirm_password = en7.get()
    
    # Connecting to MySQL database
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="userdata")

    mycursor = mydb.cursor()

    # Inserting data into the database
    sql = "INSERT INTO users (name, email, contact_number, gender, state, password) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name, email, contact_number, gender, state, password)
    mycursor.execute(sql, val)

    # Committing the transaction
    mydb.commit()

    # Closing the database connection
    mydb.close()

     # Display success message
    messagebox.showinfo("Success", "Registration Successful!")

    # Clear all entry fields
    en1.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    en6.delete(0, END)
    en7.delete(0, END)

# GUI setup
base = Tk()
base.geometry("500x500")
base.title("Registration Form")

lb1 = Label(base, text="Enter Name", width=10, font=("arial", 12))
lb1.place(x=20, y=120)
en1 = Entry(base)
en1.place(x=200, y=120)

lb3 = Label(base, text="Enter Email", width=10, font=("arial", 12))
lb3.place(x=19, y=160)
en3 = Entry(base)
en3.place(x=200, y=160)

lb4 = Label(base, text="Contact Number", width=13, font=("arial", 12))
lb4.place(x=19, y=200)
en4 = Entry(base)
en4.place(x=200, y=200)

lb5 = Label(base, text="Select Gender", width=15, font=("arial", 12))
lb5.place(x=5, y=240)
vars = IntVar()
Radiobutton(base, text="Male", padx=5, variable=vars, value=1).place(x=180, y=240)
Radiobutton(base, text="Female", padx=10, variable=vars, value=2).place(x=240, y=240)
Radiobutton(base, text="Others", padx=15, variable=vars, value=3).place(x=310, y=240)

list_of_state = ("Gujarat", "Goa", "Kerala", "Rajshthan", "Punjab", "Maharashtra", "Telangana")
cv = StringVar()
drplist = OptionMenu(base, cv, *list_of_state)
drplist.config(width=15)
cv.set("Gujarat")
lb2 = Label(base, text="Select State", width=13, font=("arial", 12))
lb2.place(x=14, y=280)
drplist.place(x=200, y=275)

lb6 = Label(base, text="Enter Password", width=13, font=("arial", 12))
lb6.place(x=19, y=320)
en6 = Entry(base, show='*')
en6.place(x=200, y=320)

lb7 = Label(base, text="Re-Enter Password", width=15, font=("arial", 12))
lb7.place(x=21, y=360)
en7 = Entry(base, show='*')
en7.place(x=200, y=360)

Button(base, text="Register", width=10, command=register).place(x=200, y=400)

base.mainloop()
