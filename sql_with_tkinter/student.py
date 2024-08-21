import mysql.connector
from tkinter import *
from tkinter import messagebox 

# Function to establish database connection
def connect_db():
    global mydb, mycursor
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Enter your MySQL password here
        database="studentdb"
    )
    mycursor = mydb.cursor()

# Function to create student table if not exists
def create_table():
    mycursor.execute("CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, grade VARCHAR(10))")

# Function to add a new student record
def add_student():
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()
    sql = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    val = (name, age, grade)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Success", "Student added successfully")

# Function to view all student records
# Function to view all student records
def view_students():
    mycursor.execute("SELECT * FROM students")
    records = mycursor.fetchall()
    student_list.delete(0, END)  # Clear the listbox
    if len(records) == 0:
        messagebox.showinfo("Empty", "No student records found")
    else:
        for record in records:
            student_list.insert(END, record)

# Function to clear all fields
def clear_fields():
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    grade_entry.delete(0, END)

# Function to delete a student record
def delete_student():
    selected_student = student_list.curselection()
    if not selected_student:
        messagebox.showinfo("Error", "Please select a student to delete")
    else:
        index = selected_student[0]
        student_id = student_list.get(index)[0]
        mycursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        mydb.commit()
        messagebox.showinfo("Success", "Student deleted successfully")
        view_students()

# Function to update a student record
def update_student():
    selected_student = student_list.curselection()
    if not selected_student:
        messagebox.showinfo("Error", "Please select a student to update")
    else:
        index = selected_student[0]
        student_id = student_list.get(index)[0]
        name = name_entry.get()
        age = age_entry.get()
        grade = grade_entry.get()
        sql = "UPDATE students SET name=%s, age=%s, grade=%s WHERE id=%s"
        val = (name, age, grade, student_id)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Success", "Student updated successfully")
        view_students()

# Main Tkinter window
root = Tk()
root.title("Student Management System")
root.geometry("600x400")

# Database connection and table creation
connect_db()
create_table()

# Labels
Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5)
Label(root, text="Grade:").grid(row=2, column=0, padx=10, pady=5)

# Entry fields
name_entry = Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)
age_entry = Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)
grade_entry = Entry(root)
grade_entry.grid(row=2, column=1, padx=10, pady=5)

# Student listbox
student_list = Listbox(root, width=70)
student_list.grid(row=0, column=2, rowspan=4, padx=20, pady=5)

# Buttons
Button(root, text="Add Student", command=add_student).grid(row=3, column=0, padx=10, pady=5)
Button(root, text="View Students", command=view_students).grid(row=3, column=1, padx=10, pady=5)
Button(root, text="Clear Fields", command=clear_fields).grid(row=3, column=2, padx=10, pady=5)
Button(root, text="Delete Student", command=delete_student).grid(row=4, column=0, padx=10, pady=5)
Button(root, text="Update Student", command=update_student).grid(row=4, column=1, padx=10, pady=5)

root.mainloop()
