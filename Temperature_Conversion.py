import tkinter as tk
from tkinter import messagebox

def celsius_to_fahrenheit_convertor(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin_convertor(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius_convertor(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin_convertor(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius_convertor(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit_convertor(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def temperature_convert():
    try:
        temperature = float(entry_value.get())
        unit = unit_var.get()

        if unit == 'C':
            fahrenheit = celsius_to_fahrenheit_convertor(temperature)
            kelvin = celsius_to_kelvin_convertor(temperature)
            result_label.config(text=f"{temperature}°C = {fahrenheit:.2f}°F = {kelvin:.2f}K",bg='orange',font=("Copperplate Gothic Light",12,"bold"))
        elif unit == 'F':
            celsius = fahrenheit_to_celsius_convertor(temperature)
            kelvin = fahrenheit_to_kelvin_convertor(temperature)
            result_label.config(text=f"{temperature}°F = {celsius:.2f}°C = {kelvin:.2f}K",bg='orange',font=("Copperplate Gothic Light",12,"bold"))
        elif unit == 'K':
            celsius = kelvin_to_celsius_convertor(temperature)
            fahrenheit = kelvin_to_fahrenheit_convertor(temperature)
            result_label.config(text=f"{temperature}K = {celsius:.2f}°C = {fahrenheit:.2f}°F",bg='orange',font=("Copperplate Gothic Light",12,"bold"))
        else:
            messagebox.showerror("Invalid Input", "Please select a valid unit.")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid temperature value.")

# Creating the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x350")

frame = tk.Frame(root, bg='lightblue')
frame.place(relwidth=1, relheight=1)

# Temperature value entry
entry_label = tk.Label(root, text="Enter temperature value:")
entry_label.config(font=("Georgia",12,"bold"))
entry_label.pack(pady=10)

entry_value = tk.Entry(root)
entry_value.config(width=35)
entry_value.pack(pady=5)

# Unit selection
unit_var = tk.StringVar(value="C")
celsius_radio = tk.Radiobutton(root, text="Celsius (°C)", variable=unit_var, value="C",bg='grey')
celsius_radio.config(font=("Georgia",10,"bold"))
fahrenheit_radio = tk.Radiobutton(root, text="Fahrenheit (°F)", variable=unit_var, value="F",bg='grey')
fahrenheit_radio.config(font=("Georgia",10,"bold"))
kelvin_radio = tk.Radiobutton(root, text="Kelvin (K)", variable=unit_var, value="K",bg='grey')
kelvin_radio.config(font=("Georgia",10,"bold"))

celsius_radio.pack(pady=5)
fahrenheit_radio.pack(pady=5)
kelvin_radio.pack(pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=temperature_convert)
convert_button.config(font=("Georgia",12,"bold"))
convert_button.pack(pady=20)

# Result display
result_label = tk.Label(root, text="",bg='lightblue')
result_label.pack(pady=20)

# Running the GUI loop
root.mainloop()