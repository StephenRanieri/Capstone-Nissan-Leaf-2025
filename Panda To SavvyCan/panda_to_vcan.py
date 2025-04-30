import time
from panda import Panda
import can
from opendbc.car.structs import CarParams

# Set up Panda
p = Panda()
p.set_safety_mode(CarParams.SafetyModel.allOutput)
p.set_can_speed_kbps(0, 500)  # Change to your bus speed if needed

# Set up virtual CAN interface
can_bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

print("Forwarding Panda CAN data to vcan0...")

while True:
    msgs = p.can_recv()
    for msg in msgs:
        can_id, data, bus = msg
        can_msg = can.Message(arbitration_id=can_id, data=bytearray(data), is_extended_id=False)
        try:
            can_bus.send(can_msg)
        except can.CanError:
            print("CAN message send failed")
    time.sleep(0.01)