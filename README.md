# PRODIGY_SD_01
## **Temperature Conversion Tool**

## Overview
This Python-based GUI application, built using Tkinter, converts temperatures between Celsius (°C), Fahrenheit (°F), and Kelvin (K). Users can input a temperature, select the unit, and receive conversions to the other two scales.

## Features
- Convert temperatures between Celsius, Fahrenheit, and Kelvin.
- Clear, user-friendly interface.
- Handles invalid inputs with error messages.
- Real-time conversion and display of results.

## Requirements
- Python installed (Tkinter included by default).

## Installation Steps:
1. **Ensure Python is installed**: Download from Python's official site.
2. **Download the script**: Save the temperature converter Python script.
3. **Run the script**: Use the following command to start the application:(e.g., `python temperature_converter.py`)

## Code Explanation

### 1. Conversion Functions:
The application includes functions for temperature conversion between the three units:
- `celsius_to_fahrenheit_convertor(celsius)`
- `celsius_to_kelvin_convertor(celsius)`
- `fahrenheit_to_celsius_convertor(fahrenheit)`
- `fahrenheit_to_kelvin_convertor(fahrenheit)`
- `kelvin_to_celsius_convertor(kelvin)`
- `kelvin_to_fahrenheit_convertor(kelvin)`

### 2. Main GUI Components:
- **Entry Field**: For temperature input.
- **Radio Buttons**: Select the temperature unit.
- **Convert Button**: Triggers the conversion.
- **Result Label**: Displays the converted values in real-time.

### 3. Error Handling:
The application displays an error message for invalid inputs (e.g., non-numeric values) using: 
'messagebox.showerror("Invalid Input", "Please enter a valid temperature value.")


### 4. Running the GUI:
The application uses `root.mainloop()` to initiate the Tkinter event loop and maintain an interactive, responsive window.

## How to Use
1. Enter a temperature value in the input field.
2. Select the unit (Celsius, Fahrenheit, or Kelvin).
3. Click the "Convert" button.
4. The results will be displayed in the corresponding units.

## Example:
For a temperature of 100°C, the output will be: (100.0°C = 212.00°F = 373.15K)

## Customization
You can modify the appearance of the application by adjusting the colors, fonts, and layout in the Tkinter widget configuration.

## Author
This application was created as a basic project to demonstrate GUI programming in Python using the Tkinter library.

## License
This project is open-source and free to use, modify, and distribute.


