# Digital Twin with Secure Data Transmission Using AES-GCM and MQTT

## Overview

This project demonstrates a basic **Digital Twin** setup where sensor data (temperature and humidity) is securely sent from a simulated sensor to a digital twin receiver using:

- **AES-GCM encryption** for confidentiality and integrity of data.
- **MQTT protocol** for lightweight, real-time communication.

The sensor encrypts data using AES-GCM with a 128-bit key and a random 12-byte nonce. The nonce is prepended to the encrypted payload and sent over MQTT. The digital twin client receives the encrypted message, extracts the nonce, and decrypts the data securely.

---

## Components

- **sensor.py**: Simulates a sensor publishing encrypted temperature and humidity data every 2 seconds.
- **digital_twin.py**: Subscribes to the MQTT topic, receives encrypted data, decrypts it, and displays the original sensor readings.

---

## Features

- Uses **AES-GCM** authenticated encryption to ensure confidentiality and message integrity.
- Uses **MQTT** (broker: `broker.hivemq.com`) for lightweight publish/subscribe messaging.
- Graceful handling of keyboard interrupts for clean shutdown.
- Prepending nonce to the encrypted message to allow proper decryption.

---

## Requirements

- Python 3.7+
- `paho-mqtt` Python package
- `cryptography` Python package

Install dependencies with:

```bash
pip install paho-mqtt cryptography
python digital_twin.py
python sensor.py
Code Highlights
Encryption (sensor.py)
AES-GCM with 128-bit key.

Random 12-byte nonce generated per message.

Nonce prepended to ciphertext.

Decryption (digital_twin.py)
Extract nonce from first 12 bytes.

Use nonce + key to decrypt and verify message.

Next Steps / Improvements
Secure key exchange between sensor and digital twin.

Add device authentication.

Store data in database or visualize with dashboard.

Extend to multiple sensor types.

Integrate with Garuda Sentinel encryption style for enhanced cybersecurity.


