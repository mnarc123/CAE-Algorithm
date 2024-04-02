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



import os
from context_encryption7 import derive_secure_key, encrypt_data_aes_gcm, decrypt_data_aes_gcm, get_enhanced_contextual_data
from e2e_encryption import generate_rsa_key_pair, encrypt_data_with_e2e

def test_context_aware_encryption():
    print("Testing Context-Aware Encryption...\n")

    # Simulate gathering contextual data
    contextual_data = get_enhanced_contextual_data()

    # Derive a secure key based on contextual data
    key, salt = derive_secure_key(contextual_data)
    print(f"Derived key (sample): {key[:16].hex()}...\n")

    # Define a plaintext message
    plaintext = "Sensitive information requiring encryption."

    # Encrypt the plaintext using the derived key
    encrypted_data, iv = encrypt_data_aes_gcm(plaintext, key)
    print(f"Encrypted data (AES-GCM): {encrypted_data.hex()}\n")

    # Decrypt the encrypted data
    decrypted_data = decrypt_data_aes_gcm(encrypted_data, key, iv)
    print(f"Decrypted data: {decrypted_data}\n")

    assert plaintext == decrypted_data, "Context-Aware Encryption: Decryption failed, plaintext does not match decrypted data."

def test_e2e_encryption():
    print("Testing End-to-End (E2E) Encryption...\n")

    # Generate RSA key pair
    private_pem, public_pem = generate_rsa_key_pair()

    # Define a plaintext message
    plaintext = "End-to-end encrypted message."

    # Encrypt the data using the recipient's public key
    encrypted_data, iv, encrypted_aes_key = encrypt_data_with_e2e(plaintext, public_pem)
    print(f"Encrypted data (sample): {encrypted_data[:16].hex()}...\n")

    # Normally, the decryption process would be performed by the recipient
    # who possesses the corresponding private key. This example does not
    # include RSA decryption for brevity. Refer to the RSA decryption
    # documentation for details on how to decrypt the AES key and then
    # decrypt the message.

    print("E2E Encryption test completed. Note: Decryption step not included in this example.\n")

if __name__ == "__main__":
    test_context_aware_encryption()
    test_e2e_encryption()
