# Step by Step: Stream Black Panda Data into SavvyCAN using a Linux Operating System  
**By Stephen Ranieri**

## Prerequisites:  
- Python Downloaded  
- Linux System  
- SavvyCan  

---

## Step 1: Open Terminal on Linux Operating System  
Run the following commands in the terminal in order to create and activate vcan0:

```bash
sudo modprobe vcan  
sudo ip link add dev vcan0 type vcan  
sudo ip link set up vcan0  
```

To test to make sure it works you can run the following command:

```bash
ip link show vcan0  
```

If it works correctly you should see something similar to the following response:  
**Vcan0: <NOARP, UP, LOWER_UP> mtu …**

---

## Step 2: Connect to the Black Panda and Forward Data  

Plug in black panda to ADAS system via usb and car harness  

Use the python file `panda_to_vcan.py` in order to start forwarding data to the vcan0 link  

To do this open terminal and execute the following command inside the directory that the file is located in:

```bash
python panda_to_vcan.py  
```

---

## Step 3: Open SavvyCan and Connect to vcan0  

Launch SavvyCan  

Within SavvyCan:  
Click `connection > Open connection window > Add New Device Connection > QT SerialBus Devices (SocketCAN, PeakCan, etc)`  

Then underneath **SerialBus Device Type** drop down select **socket can**, in **port** select `vcan0`

---

## Notes:  
- Savvy CAN will not log unless `panda_to_vcan.py` is running  
- Savvy CAN will only log data from the specific bus you are connected to  
- Car Harness can only natively connect to the ADAS system  
- Future use case would be to connect to other ECUs  
  - i.e Body Control Module (BCM)  
