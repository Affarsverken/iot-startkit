import socket
import time
import binascii

from network import LoRa
from machine import Pin

# initialize pin `P23` as an input pin
door_pin = Pin('P23', mode=Pin.IN, pull=Pin.PULL_UP)

# initialize LORAWAN mode for EU region
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# print DevEUI of the device, use this when provisioning it in your network server
print("DevEUI: " + binascii.hexlify(lora.mac()).decode('utf-8').upper())

# OTAA authentication parameters, replace these with your own
app_eui = binascii.unhexlify('70B3D57ED000FF4A')
app_key = binascii.unhexlify('9BD68F284A13699C5B0CB03C8DE25AEE')

print("Joining network using OTAA (Over the Air Activation)")
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')

print("Joined network")


def send(data):
    # create socket to be used for LoRa communication
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

    # configure data rate
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

    # make the socket blocking
    # (waits for the data to be sent and for the 2 receive windows to expire)
    s.setblocking(True)

    # uplink data to send
    print("Sending uplink", binascii.hexlify(data).decode("utf-8"))
    s.send(data)
    print("Uplink sent")


last_value = -1

while True:
    # read pin value
    current_value = door_pin.value()

    if(current_value != last_value):
        # pin has changed since last check
        last_value = current_value

        # send LoRa message
        send(bytes([current_value]))

        if(current_value == 1):
            print("Door was opened")
        else:
            print("Door was closed")

    time.sleep(1)
