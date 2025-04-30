
# Serial Command Toolkit for CAN and UART Communication

This repository contains a set of Python scripts to interface with both UART and CAN communication systems. It includes a graphical interface for UART command sending and tools to send and log CAN messages using the Panda device.

---

## Contents

- [`serial_command_gui.py`](#serial_command_gui.py) — GUI to send UART hex commands to an embedded device
- [`sentMessages.py`](#sentmessagespy) — Continuously sends a predefined CAN message to the vehicle via Panda
- [`setupPanda.py`](#setuppandapy) — Logs all CAN traffic from the vehicle and saves it to a CSV file

---

## `serial_command_gui.py`

###  What It Does

This script creates a Tkinter GUI with four buttons. When a button is clicked, it sends a corresponding hexadecimal command over a serial port (UART). It also continuously listens for incoming serial data and prints it to the terminal. The serial connection closes automatically when the GUI exits.

###  Use Case

Useful for sending commands to a microcontroller or embedded system, such as activating peripherals, sending debug instructions, or simulating UART communication.

###  Requirements

- Python 3.x
- [`pyserial`](https://pypi.org/project/pyserial/)

```bash
pip install pyserial
```

---

## `sentMessages.py`

### 🔧 What It Does

This script uses the [Comma.ai Panda](https://comma.ai/panda/) hardware to **continuously send a specific CAN message (ID 0x1CB)** to a connected vehicle on bus 0. It sets the Panda into "allOutput" mode to allow message injection and runs in an infinite loop until interrupted.

###  Use Case

Used to simulate or test CAN message reception by the car’s ECUs (e.g., mimicking button presses, sensor data, or spoofing vehicle behavior).

###  Requirements

- Python 3.x
- [`panda`](https://pypi.org/project/panda/)
- `opendbc` from Comma.ai

```bash
pip install panda
```

---

## `setupPanda.py`

###  What It Does

This script captures **live CAN messages** from the vehicle via the Panda device and writes them to a CSV file. It records the timestamp, CAN bus number, message ID, and payload data. The loop runs until manually interrupted with `Ctrl+C`.

###  Use Case

Helps reverse-engineer vehicle behavior by logging CAN traffic while interacting with the car (e.g., turning on lights, opening doors). The CSV file can be analyzed later to identify which CAN IDs and data patterns correspond to specific actions.

###  Requirements

- Python 3.x
- [`panda`](https://pypi.org/project/panda/)

---

## Example CSV Output (`test.csv`)

```
timestamp,bus,address,data
1714529800.1234,0,0x1CB,0000000014000000
1714529800.1345,0,0x2F3,deadbeefcafebabe
...
```

---

## License

This project is open for educational and non-commercial use. Modify and expand freely.
