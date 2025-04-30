import csv
import time
from panda import Panda

# Connect to Panda
p = Panda()

# Open a CSV file to write
with open('test.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write CSV headers
    writer.writerow(['timestamp', 'bus', 'address', 'data'])

    print("Logging CAN data... Press CTRL+C to stop.")

    try:
        while True:
			# Receive CAN messages
            msgs = p.can_recv()
            now = time.time()
            for address, data, bus in msgs:
                # Write each message to the CSV
                writer.writerow([now, bus, hex(address), data.hex()])
            time.sleep(0.01)  # Slight delay to reduce CPU usage
    except KeyboardInterrupt:
        print("Logging stopped.")
