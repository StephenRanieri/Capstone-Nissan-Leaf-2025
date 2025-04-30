from opendbc.car.structs import CarParams
import time
from panda import Panda

panda = Panda()
panda.set_safety_mode(CarParams.SafetyModel.allOutput)
try:
	while True:
		panda.can_send(0x1CB, b'0000000014000000', 0)
		time.sleep(0.01)  # Slight delay to reduce CPU usage
except KeyboardInterrupt:
	print("Logging stopped.")
