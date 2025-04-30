
# Serial Command Toolkit for CAN and UART Communication

This repository contains a set of Python scripts to interface with both UART and CAN communication systems. It includes a graphical interface for UART command sending and tools to send and log CAN messages using the Panda device.

---

## Contents

- [`serial_command_gui.py`](#serial_command_gui.py): GUI for sending UART hex commands
- [`sentMessages.py`](#sentmessagespy): Script to repeatedly send a CAN message via Panda
- [`setupPanda.py`](#setuppandapy): Script to log incoming CAN messages to a CSV file

---

## `serial_command_gui.py`

### Description

A Python-based graphical user interface (GUI) to send predefined hexadecimal commands over a serial port using buttons. It also monitors the serial port for incoming data and prints responses to the terminal.

### Features

- GUI with four buttons
- Configurable serial port and baud rate (default: COM4 @ 9600)
- Real-time monitoring of UART input
- Auto-closes the port on exit

### Requirements

- Python 3.x
- [`pyserial`](https://pypi.org/project/pyserial/)

```bash
pip install pyserial
```

### Command Mapping

| Button   | Command Sent                            | ASCII Equivalent |
|----------|------------------------------------------|------------------|
| Button 1 | `b'\x41\x42\x43\x44\x48\x65\x6c\x6c\x6f'` | ABCDHello        |
| Button 2 | `b'\x31\x32\x33\x34'`                    | 1234             |
| Button 3 | `b'\x55\x56\x57\x58'`                    | UVWX             |
| Button 4 | `b'\x61\x62\x63\x64'`                    | abcd             |

---

## `sentMessages.py`

### Description

This script sends a fixed CAN message repeatedly using the [Panda](https://comma.ai/panda/) device.

### Requirements

- Python 3.x
- `panda` library
- `opendbc`

```bash
pip install panda
```

### Code Summary

```python
from opendbc.car.structs import CarParams 
import time
from panda import Panda

panda = Panda()
panda.set_safety_mode(CarParams.SafetyModel.allOutput)

try:
    while True:
        panda.can_send(0x1CB, b'0000000014000000', 0)
        time.sleep(0.01)
except KeyboardInterrupt:
    print("Logging stopped.")
```

---

## `setupPanda.py`

### Description

This script logs incoming CAN traffic from the Panda device and writes it to a CSV file for analysis.

### Output Format

CSV with columns:
- Timestamp
- Bus
- Address (in hex)
- Data (in hex)

### Code Summary

```python
import csv
import time
from panda import Panda

p = Panda()

with open('test.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['timestamp', 'bus', 'address', 'data'])

    print("Logging CAN data... Press CTRL+C to stop.")

    try:
        while True:
            msgs = p.can_recv()
            now = time.time()
            for address, data, bus in msgs:
                writer.writerow([now, bus, hex(address), data.hex()])
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("Logging stopped.")
```

---

## License

This project is open for educational and non-commercial use. Modify and expand freely.
