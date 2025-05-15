import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import paho.mqtt.client as mqtt
from key import KEY
import json

TOPIC = "sensor/data"
BROKER = "localhost"
PORT = 1883

def decrypt_data(enc_data_b64, key):
    try:
        enc_data = base64.b64decode(enc_data_b64)
        nonce = enc_data[:12]
        ct = enc_data[12:]
        aesgcm = AESGCM(key)
        data = aesgcm.decrypt(nonce, ct, None)
        return data.decode()
    except Exception as e:
        print("Decryption error:", e)
        return None

def on_connect(client, userdata, flags, rc):
    print("Connected to broker.")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    enc_payload = msg.payload.decode()
    print(f"Received Encrypted: {enc_payload}")
    decrypted = decrypt_data(enc_payload, KEY)
    if decrypted:
        try:
            sensor_data = json.loads(decrypted)
            print("Decrypted Sensor Data:", sensor_data)
        except json.JSONDecodeError:
            print("Decrypted data not JSON:", decrypted)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()
