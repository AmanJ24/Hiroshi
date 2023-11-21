from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    #Checking if the fields are empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Oops", message = "Please don't leave any fields empty!")
    else:
        #Working with the file
        try:
            with open("data.json", mode="r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file: 
                json.dump(new_data, data_file, indent=4)
        else:           
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                #Saving updated data    
                json.dump(data, data_file, indent = 4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
        website_name = website_entry.get()
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title = "Error", message = "No Data File Found.")
        else:    
            if website_name in data:
                email = data[website_name]["email"]
                password = data[website_name]["password"]
                messagebox.showinfo(title = website_name, message = f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title = "Error", message = f"No Details for {website_name} exists.")    
            
# ---------------------------- UI SETUP ------------------------------- #
#Screen setup
window = Tk()
window.title("Password manager")
window.config(padx = 50, pady = 50)

#Image setup
canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
lock_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = lock_img)
canvas.grid(row = 0, column = 1)

#Labels
website_label = Label(text = "Website:")
website_label.grid(row = 1, column = 0)
email_label = Label(text = "Email/Username:")
email_label.grid(row = 2, column = 0 )
password_label = Label(text = "Password:")
password_label.grid(row = 3, column = 0)

#Entries
website_entry = Entry(width = 17)
website_entry.grid(row = 1, column = 1)
website_entry.focus()
email_entry = Entry(width = 35)
email_entry.grid(row = 2, column = 1, columnspan = 2)
email_entry.insert(0, "amanjangir@gmail.com")
password_entry = Entry(width = 17)
password_entry.grid(row = 3, column = 1)

#Buttons
search_button = Button(text = "Search", width = 14, command = find_password)
search_button.grid(row = 1, column = 2)
generate_password_button = Button(text = "Generate Password", width = 14, command = generate_password)
generate_password_button.grid(row = 3, column = 2)
add_button = Button(text = "Add", width = 30, command = save)
add_button.grid(row = 4, column = 1, columnspan = 2)

#Keeping the screen on 
window.mainloop()