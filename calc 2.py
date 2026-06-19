from tkinter import *

root = Tk()
root.title("Modern Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#1E1E1E")

expression = ""

# ---------- Functions ----------
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# ---------- Display ----------
equation = StringVar()

display = Entry(
    root,
    textvariable=equation,
    font=("Segoe UI", 28),
    justify="right",
    bd=0,
    bg="#252526",
    fg="white",
    insertbackground="white"
)

display.grid(row=0, column=0, columnspan=4,
             sticky="nsew", padx=10, pady=15, ipady=20)

# ---------- Button Style ----------
btn_font = ("Segoe UI", 16)

def create_button(text, row, col, bg, command):
    Button(
        root,
        text=text,
        font=btn_font,
        bg=bg,
        fg="white",
        activebackground="#555555",
        activeforeground="white",
        bd=0,
        relief=FLAT,
        command=command
    ).grid(
        row=row,
        column=col,
        sticky="nsew",
        padx=5,
        pady=5
    )

# ---------- Buttons ----------
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
]

for text, row, col in buttons:

    if text in ['+', '-', '*', '/']:
        color = "#FF9500"   # Orange operators

    elif text == "=":
        color = "#28A745"   # Green equals

    elif text == "C":
        color = "#DC3545"   # Red clear

    else:
        color = "#3A3A3A"   # Number buttons

    if text == "=":
        create_button(text, row, col, color, equal)

    elif text == "C":
        create_button(text, row, col, color, clear)

    else:
        create_button(
            text,
            row,
            col,
            color,
            lambda t=text: press(t)
        )

# ---------- Responsive Grid ----------
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
