from tkinter import *

# Step 1: Create window
window = Tk()
window.geometry('300x450')
window.title("Calculator")

# Step 2: Entry widget
entry = Entry(window, width=25, borderwidth=5, font=('Arial', 18), justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Step 3: Functions
def button_click(value):
    entry.insert(END, value)

def clear_entry():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Step 4: Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('clr', 5, 0)
]

for (text, row, col) in buttons:
    if text == 'clr':
        cmd = clear_entry
    elif text == '=':
        cmd = calculate
    else:
        cmd = lambda t=text: button_click(t)

    Button(window, text=text, width=10, height=2, font=('Arial', 12), command=cmd)\
        .grid(row=row, column=col, padx=5, pady=5)

# Step 5: Run the app
window.mainloop()
