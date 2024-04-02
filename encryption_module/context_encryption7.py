# Copyright 2024 Marco Narcisi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import datetime
import socket
import os
import getpass
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes, aead
from cryptography.hazmat.primitives.asymmetric import padding as oaep_padding, rsa
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.asymmetric import rsa
from concurrent.futures import ThreadPoolExecutor
import secrets

def safe_get_hostname():
    try:
        return socket.gethostname()
    except Exception:
        return "unknown_host"

def safe_get_ip_address(hostname):
    try:
        return socket.gethostbyname(hostname)
    except Exception:
        return "unknown_ip"

def safe_get_os_name():
    try:
        return os.name
    except Exception:
        return "unknown_os"

def get_enhanced_contextual_data():
    hostname = safe_get_hostname()
    return {
        'device_usage': 'high',
        'location_access_frequency': 5,
        'current_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'user': getpass.getuser(),
        'hostname': hostname,
        'ip_address': safe_get_ip_address(hostname),
        'os': safe_get_os_name()
    }

def serialize_context(contextual_data):
    return os.urandom(16)  # Using random data for each encryption operation enhances security.

def derive_secure_key(contextual_data, length=32):
    """Derives a secure key from contextual data using PBKDF2 with SHA-256 and a cryptographically secure salt."""
    salt = secrets.token_bytes(16)  # Use a secure random salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=length,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(serialize_context(contextual_data))
    return key, salt

def encrypt_data_aes_gcm(data, key):
    """Encrypts data using AES-GCM."""
    aesgcm = aead.AESGCM(key)
    iv = secrets.token_bytes(12)  # AES-GCM typically uses a 12-byte IV
    encrypted_data = aesgcm.encrypt(iv, data.encode('utf-8'), None)
    return encrypted_data, iv

def decrypt_data_aes_gcm(encrypted_data, key, iv):
    """Decrypts data using AES-GCM."""
    aesgcm = aead.AESGCM(key)
    try:
        decrypted_data = aesgcm.decrypt(iv, encrypted_data, None)
        return decrypted_data.decode('utf-8')
    except Exception as e:
        raise ValueError(f"Decryption failed: {e}")

def generate_rsa_key_pair():
    """Generates an RSA key pair for asymmetric encryption use cases."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def simulate_encryption_process():
    """Simulates the encryption process, integrating E2E encryption with AES-GCM."""
    contextual_data = get_enhanced_contextual_data()
    key, _ = derive_secure_key(contextual_data)
    plaintext = "Sensitive information requiring encryption."
    encrypted_data, iv = encrypt_data_aes_gcm(plaintext, key)
    print(f"Encrypted data: {encrypted_data.hex()}")  # Print the encrypted data in hexadecimal format
    decrypted_data = decrypt_data_aes_gcm(encrypted_data, key, iv)
    print(f"Decrypted data: {decrypted_data}")  # Print the decrypted data
    assert plaintext == decrypted_data, "Decryption failed, plaintext does not match decrypted data."

if __name__ == "__main__":
    simulate_encryption_process()
