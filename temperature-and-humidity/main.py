import socket
import time
import binascii
import dht

from network import LoRa
from machine import Pin

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

# create socket to be used for LoRa communication
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# configure data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)


def send(data):
    # send a byte array over LoRaWAN
    print("Sending uplink", binascii.hexlify(data).decode("utf-8"))
    s.send(data)
    print("Uplink sent")


# initialize pin `G10` as sensor pin
dht_pin = Pin('G10', mode=Pin.OPEN_DRAIN)

while True:
    # read temperature (celcius) and humidity (percent)
    temp, hum = dht.DHT22(dht_pin)
    temp_str = '{}.{}'.format(temp//10, temp % 10)
    hum_str = '{}.{}'.format(hum//10, hum % 10)

    # create string to send
    uplink = '{} {}'.format(temp_str, hum_str)

    # convert ascii to hex values and send over LoRaWAN
    send(bytearray(uplink))
    time.sleep(60)  # repeat every minute
