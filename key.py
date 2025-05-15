from cryptography.hazmat.primitives.ciphers.aead import AESGCM

KEY = AESGCM.generate_key(bit_length=128)  # generate once and reuse
