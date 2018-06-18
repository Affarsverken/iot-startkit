# Affärsverken IOT Startkit

This repository contains a few code examples to get started with Affärsverkens IOT Startkit.

## Hardware

The startkit contains the following components:

- Pycom LoPy4
- Pycom Expansion Board 2.0
- Pycom LoRa Antenna
- Magnetic Contact Switch
- PIR (motion) Sensor - `HC-SR501`
- Temperature and Humidity Sensor - `DHT22` incl. 4.7K - 10K pullup resistor
- Breadboard
- Jumper Wires

## Software

To modify and upload the examples to a LoPy it is recommended to install the Pymakr plugin for either [Visual Studio Code](https://code.visualstudio.com/) or [Atom](https://atom.io/)

See the following link for instructions on how to set up your development environment:

https://docs.pycom.io/chapter/gettingstarted/installation/pymakr.html

## Code examples

- `quick-start` - Hello World, a minimal example of how to join a LoRaWAN network and send your first uplink package
- `door-sensor` - Send an uplink when a door is opened or closed
- `motion-detection` - Send an uplink when movement is detected
- `temperature-and-humidity` - Periodically send temperature and humidity values
