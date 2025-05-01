import tkinter as tk
from panda import Panda
from opendbc.car.structs import CarParams

# Initialize Panda
panda = Panda()
panda.set_safety_mode(CarParams.SafetyModel.allOutput)

# Function to send the CAN message once
def send_can_message():
    try:
        # Send the message (converted to proper byte format)
        panda.can_send(0x1CB, b'\x00\x00\x00\x00\x14\x00\x00\x00', 0)
        print("CAN message sent.")
    except Exception as e:
        print("Error:", e)

# GUI setup
root = tk.Tk()
root.title("CAN Message Sender")
root.geometry("300x200")

send_button = tk.Button(root, text="Send CAN Command", command=send_can_message,
                        font=("Arial", 14), bg="green", fg="white", padx=10, pady=10)
send_button.pack(expand=True)

root.mainloop()
