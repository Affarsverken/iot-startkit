import socket
import time
import binascii

from network import LoRa

# initialize LORAWAN mode for EU region
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# print DevEUI of the device, use this when provisioning it in your network server
print("DevEUI: " + binascii.hexlify(lora.mac()).decode('utf-8').upper())

# OTAA authentication parameters, replace these with your own
app_eui = binascii.unhexlify('0DAEE5D7675577E5')
app_key = binascii.unhexlify('78346FD867A816645B66577964B230B5')

print("Joining network using OTAA (Over the Air Activation)")
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')

print("Joined network")

# create socket to be used for LoRa communication
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# configure data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)

# uplink data to send
uplink = bytes([0x01])

print("Sending uplink", binascii.hexlify(uplink).decode("utf-8"))
s.send(uplink)
