# Affärsverken IOT Startkit

This repository contains a few code examples to get started with Affärsverkens IOT Startkit.

## Hardware

The startkit contains the following components:

-   Pycom LoPy4
-   Pycom Expansion Board 2.0
-   Pycom LoRa Antenna
-   Magnetic Contact Switch
-   PIR (motion) Sensor - `HC-SR501`
-   Temperature and Humidity Sensor - `DHT22` incl. 4.7K - 10K pullup resistor
-   Breadboard
-   Jumper Wires

## Software

### Firmware updater

Link to Pycom Firmware Updater

### IDE

To modify and upload the examples to a LoPy it is recommended to install the Pymakr plugin for either [Visual Studio Code](https://code.visualstudio.com/) or [Atom](https://atom.io/)

See the following link for instructions on how to set up your development environment:

https://docs.pycom.io/chapter/gettingstarted/installation/pymakr.html

Once you have your editor set up, go into the Pymakr Global Settings and set your

## Getting started

Before you can get started you need to register your device on The Things Network (TTN).
Go to https://console.thethingsnetwork.org/applications and add an application for your startkit.

Then go into the newly created application and register your LoPy4 device.
Device ID can be set to anything you like, but Device EUI has to match your specific LoRa module. See the next section for details on how to do that.

### Figuring out Device EUI

To find out the Device EUI of your LoPy4, connect to device console in your Pymakr editor (see the [Software](#software) section)

Once you have a console open and can see the `>>>` prompt, paste the following code (also found in the file `get_deveui.py`):

```
from network import LoRa
import binascii
lora = LoRa()
print(binascii.hexlify(lora.mac()).decode())
```

Example output:

```
>>> print(binascii.hexlify(lora.mac()).decode())
0123456789abcdef
```

Where `0123456789abcdef` would be your Device EUI.

## Code examples

-   `quick-start` - A minimal example of how to join a LoRaWAN network and send your first uplink package
-   `door-sensor` - Send an uplink when a door is opened or closed
-   `motion-detector` - Send an uplink when movement is detected
-   `temperature-and-humidity` - Periodically send temperature and humidity values
