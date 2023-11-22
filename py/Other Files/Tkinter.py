from tkinter import *

FONT = ("Arial","12")

def button_clicked():
    value = enter.get()
    new_value = round(int(value) * 1.60934)
    label_3.config(text = str(new_value))

window = Tk()
window.title("Miles to Km Converter")
window.config(padx = 20, pady = 20)

my_label = Label(text = "Miles", font = FONT)
my_label.grid(column = 3, row = 0)

enter = Entry(width = 10)
enter.grid(column = 2, row = 0)

label_2 = Label(text = "is equal to", font = FONT)
label_2.grid(column = 0, row =1)

label_3 = Label(text = "0", font = FONT)
label_3.grid(column = 2, row = 1)

label_4 = Label(text = "Km", font = FONT)
label_4.grid(column = 3, row = 1)

button = Button(text = "Button", command = button_clicked)
button.grid(column = 2, row = 2)


window.mainloop()


# def add(*args):
#     result = 0
#     for n in args:
#         result += n
#     print(result)

# add(3, 5, 6, 5)


# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)

# calculate(2, add = 3, multiply = 5)    