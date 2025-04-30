Serial Command Sender GUI
=========================

Description
-----------
This is a Python-based graphical user interface (GUI) that allows users to send predefined hexadecimal commands over a serial port using buttons. It also monitors the serial port for incoming data and displays responses in the terminal.

The GUI is built using Tkinter, and serial communication is handled using the PySerial library. This tool is useful for interacting with embedded devices, development boards, or systems using UART communication.

Features
--------
- GUI with four buttons, each sending a different predefined command
- Configurable serial port and baud rate (default: COM4 @ 9600 baud)
- Real-time display of incoming serial data in the terminal
- Automatically closes the serial port when the application exits

Requirements
------------
- Python 3.x
- pyserial library

To install pyserial, run:
    pip install pyserial

Usage
-----
1. Connect your target device (e.g., microcontroller) to your computer via USB.
2. Update the COM port in the script if needed (default is "COM4"):
       ser = serial.Serial("COM4", 9600, timeout=1)
3. Run the script:
       python serial_command_gui.py
4. A window will appear with four buttons. Each button sends a command when clicked.
5. Any response from the device is printed in the terminal in real time.

Command Mapping
---------------
Button 1 → b'\x41\x42\x43\x44\x48\x65\x6c\x6c\x6f'   (sends "ABCDHello")
Button 2 → b'\x31\x32\x33\x34'                       (sends "1234")
Button 3 → b'\x55\x56\x57\x58'                       (sends "UVWX")
Button 4 → b'\x61\x62\x63\x64'                       (sends "abcd")

Customization
-------------
You can change the commands sent by editing the `commands` dictionary inside the script.

To use a different COM port or baud rate, modify this line near the top:
    ser = serial.Serial("COM4", 9600, timeout=1)

You can also add more buttons by copying and adapting the button creation code.

Example Terminal Output
-----------------------
Sent: b'ABCDHello'
Incoming: b'OK'
Extra Response: b'Device Ready'

Known Issues
------------
- If the specified COM port is not found, the script will print "Failed to connect to COM4".
- The application does not currently handle reconnecting to a serial port after disconnecting.

Closing Notes
-------------
This script is intended for prototyping and testing purposes. It is a great starting point for more advanced serial GUI tools with dynamic input, logging, or device-specific command sets.

Author: [Your Name]
Date: [Date]

License
-------
This project is open for educational and non-commercial use. Modify and expand freely.
