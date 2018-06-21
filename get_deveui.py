from network import LoRa
import binascii
lora = LoRa()
print(binascii.hexlify(lora.mac()).decode())
