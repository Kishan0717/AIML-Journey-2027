import tkinter as tk

# Main Window
window = tk.Tk()
window.title("Kishan Smart Calculator")
window.geometry("400x450")
window.configure(bg="lightblue")

# Heading
heading = tk.Label(
    window,
    text="Kishan Smart Calculator",
    font=("Arial", 18, "bold"),
    bg="lightblue",
    fg="black"
)
heading.pack(pady=10)

# First Number
label1 = tk.Label(
    window,
    text="First Number",
    bg="lightblue",
    fg="black"
)
label1.pack()

entry1 = tk.Entry(window, font=("Arial", 12))
entry1.pack(pady=5)

# Second Number
label2 = tk.Label(
    window,
    text="Second Number",
    bg="lightblue",
    fg="black"
)
label2.pack()

entry2 = tk.Entry(window, font=("Arial", 12))
entry2.pack(pady=5)

# Result Label
label_result = tk.Label(
    window,
    text="Result:",
    font=("Arial", 14),
    bg="lightblue",
    fg="black"
)
label_result.pack(pady=10)

# Functions
def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        label_result.config(text=f"Result: {num1 + num2}")
    except:
        label_result.config(text="Error: Enter numbers only!")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        label_result.config(text=f"Result: {num1 - num2}")
    except:
        label_result.config(text="Error: Enter numbers only!")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        label_result.config(text=f"Result: {num1 * num2}")
    except:
        label_result.config(text="Error: Enter numbers only!")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if num2 == 0:
            label_result.config(text="Error: Cannot divide by zero!")
        else:
            label_result.config(text=f"Result: {num1 / num2}")
    except:
        label_result.config(text="Error: Enter numbers only!")

def modulus():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        label_result.config(text=f"Result: {num1 % num2}")
    except:
        label_result.config(text="Error: Enter numbers only!")

def power():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        label_result.config(text=f"Result: {num1 ** num2}")
    except:
        label_result.config(text="Error: Enter numbers only!")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    label_result.config(text="Result:")

# Buttons
button_add = tk.Button(window, text="Add", width=15, bg="green", fg="white", command=add)
button_add.pack(pady=2)

button_subtract = tk.Button(window, text="Subtract", width=15, bg="orange", fg="white", command=subtract)
button_subtract.pack(pady=2)

button_multiply = tk.Button(window, text="Multiply", width=15, bg="blue", fg="white", command=multiply)
button_multiply.pack(pady=2)

button_divide = tk.Button(window, text="Divide", width=15, bg="purple", fg="white", command=divide)
button_divide.pack(pady=2)

button_modulus = tk.Button(window, text="Modulus (%)", width=15, bg="brown", fg="white", command=modulus)
button_modulus.pack(pady=2)

button_power = tk.Button(window, text="Power (^)", width=15, bg="red", fg="white", command=power)
button_power.pack(pady=2)

button_clear = tk.Button(window, text="Clear", width=15, bg="gray", fg="white", command=clear)
button_clear.pack(pady=10)

# Run Window 
window.mainloop() 
