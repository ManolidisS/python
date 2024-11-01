from book_database import book_database
from users import users
from tkinter import *
from tkinter import messagebox
from functools import partial
from hashlib import sha256
access = False
books = []
buttons = []
labels = []

def login(userid,password):
    try:
        userid = int(userid)
    except:
        messagebox.showerror("Error", "Ensure the UserID is an integer.")
    else:
        userid = sha256((str(userid)).encode('utf-8')).hexdigest()
        password = sha256((str(password)).encode('utf-8')).hexdigest()
        for i in users:
            if userid == i["UserID"]:
                if password == i["Password"]:
                    messagebox.showinfo("Login Successful", "Welcome, %s.\nLoading the database..." % i["Role"].capitalize())
                    global access
                    access = True
                    login_window.destroy()
        if access == False:
            messagebox.showerror("Login Failed", "Invalid UserID or Password.")

def search(book_title):
    for i in buttons:
        i.destroy()
    books = []
    labels = []
    for i in book_database:
        name = i["Name"].lower().strip().split()
        for j in name:
            if j in book_title.lower().strip().split():
                books.append(i)
                break
    if books != []:
        for i in books:
            temp = partial(book_info, i)
            buttons.append(Button(window, text=(i["Name"]+" by "+i["Author"]),command=temp))
            buttons[-1].pack(padx=100,pady=2)
    else:
        messagebox.showinfo("No books found.","No books found for the given title.")

def book_info(book):
    global book_window
    book_window = Tk()
    book_window.eval('tk::PlaceWindow . center')
    book_window.resizable(False, False)
    book_window.title(book["Name"]+" Information")
    book_window.config(bg="grey")

    withdraw_button = Button(book_window, text="Withdraw Book", command= lambda:(withdraw(book)))
    withdraw_button.pack(padx=5,pady=10, side=LEFT)

    return_button = Button(book_window, text="Return Book", command= lambda:(réturn(book)))
    return_button.pack(padx=5,pady=10, side=LEFT)

    for i in book:
        labels.append(Label(book_window, text=i+": "+book[i], justify="left"))
        labels[-1].pack(padx=10,pady=5)
    
    book_window.mainloop()

def withdraw(book):
    book["Withdrawn"] = "Yes"
    labels[-1].config(text="Withdrawn: Yes")

def réturn(book):
    book["Withdrawn"] = "No"
    labels[-1].config(text="Withdrawn: No")



login_window = Tk()
login_window.eval('tk::PlaceWindow . center')
login_window.resizable(False, False)
login_window.title("Login to Library Database")
login_window.config(bg="grey")

username_label = Label(login_window, text="UserID:")
username_label.pack(padx=100,pady=2.5)
username_entry = Entry(login_window)
username_entry.pack(padx=100,pady=5)

password_label = Label(login_window, text="Passsword:")
password_label.pack(padx=100,pady=2.5)
password_entry = Entry(login_window, show="*")
password_entry.pack(padx=100,pady=5)

login_button = Button(login_window, text="Login", command = lambda: login(username_entry.get(),password_entry.get()))
login_button.pack(padx=100,pady=10)

login_window.mainloop()

if access == True:
    window = Tk()
    window.eval('tk::PlaceWindow . center')
    window.resizable(False, False)
    window.title("Library Database")
    window.config(bg="grey")

    search_label = Label(window, text="Please enter the book's title: ")
    search_label.pack(padx=100,pady=2.5)

    search_entry = Entry(window)
    search_entry.pack(padx=100,pady=5)

    search_button = Button(window, text="Search", command = lambda: search(search_entry.get()))
    search_button.pack(padx=100,pady=10)

    window.mainloop()

    with open("book_database.py", "w") as file:
        file.write(("book_database = ")+str(book_database))