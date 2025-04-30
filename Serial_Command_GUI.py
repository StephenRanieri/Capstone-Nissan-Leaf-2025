import tkinter as tk # imports tkinter for GUI
import serial # imports serial for serial communication

# --- Set up Serial Port ---
try: # Attempt to connect to the serial port
    ser = serial.Serial("COM4", 9600, timeout=1)  # Adjusts COM port and baudrate if needed
except serial.SerialException: # If connection fails, print error message
    print("Failed to connect to COM4") 
    ser = None # Set ser to None if connection fails

# --- Tkinter GUI Setup ---
root = tk.Tk() # Create the main window
root.title("Serial Command Sender")
root.geometry("600x400")  # Bigger window

# Define button click behavior
def button_click(command_bytes): # Function to handle button clicks
    if ser and ser.is_open:      # Check if serial port is available
        ser.write(command_bytes) # Send the command
        s = ser.read(len(command_bytes))  # Read the same number of bytes back
        print(f"Sent: {command_bytes}") 
        response = ser.read_all()  # Read any extra data
        if response:
            print(f"Extra Response: {response}")
    else:
        print("Serial port not available!")

# Define hex commands for each button
commands = {
    1: b'\x41\x42\x43\x44\x48\x65\x6c\x6c\x6f',  # command for button 1
    2: b'\x31\x32\x33\x34',                      # command for button 2
    3: b'\x55\x56\x57\x58',                      # command for button 3
    4: b'\x61\x62\x63\x64'                       # command for button 4
}

# Common button style
button_style = {
    "font": ("Arial", 20),
    "bg": "#87CEEB",
    "activebackground": "#00BFFF"
}

# Create 4 buttons
button1 = tk.Button(root, text="Button 1", command=lambda: button_click(commands[1]), **button_style)
button2 = tk.Button(root, text="Button 2", command=lambda: button_click(commands[2]), **button_style)
button3 = tk.Button(root, text="Button 3", command=lambda: button_click(commands[3]), **button_style)
button4 = tk.Button(root, text="Button 4", command=lambda: button_click(commands[4]), **button_style)

# Place buttons in a 2x2 grid
button1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
button2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
button3.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
button4.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

# Make the rows and columns expand equally
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

def check_serial_input():
    if ser and ser.in_waiting:
        incoming_data = ser.read(ser.in_waiting)
        print(f"Incoming: {incoming_data}")
    root.after(100, check_serial_input)  # Call again after 100 ms

# Start the background serial monitor
check_serial_input()

# Start GUI event loop
root.mainloop()

# Close serial port when window is closed
if ser and ser.is_open:
    ser.close()
