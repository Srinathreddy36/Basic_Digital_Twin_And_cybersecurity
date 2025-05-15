from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import json
import paho.mqtt.client as mqtt
import time

# Generate or use a fixed 128-bit (16 bytes) AES key
KEY = AESGCM.generate_key(bit_length=128)  # do this once and reuse this key

def encrypt_data(data: bytes, key: bytes) -> bytes:
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)  # 12-byte nonce for AES-GCM
    encrypted = aesgcm.encrypt(nonce, data, None)
    return nonce + encrypted  # prepend nonce for decryption

# MQTT setup
client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)
client.loop_start()

try:
    while True:
        sensor_data = {
            "temperature": 25.5,
            "humidity": 70
        }
        json_data = json.dumps(sensor_data).encode('utf-8')
        encrypted_data = encrypt_data(json_data, KEY)
        client.publish("digitaltwin/sensor", encrypted_data)
        print(f"Sent Encrypted: {encrypted_data.hex()}")
        time.sleep(2)

except KeyboardInterrupt:
    print("Sensor stopped by user")
    client.loop_stop()
    client.disconnect()
