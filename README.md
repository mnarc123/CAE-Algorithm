# Context-Aware Encryption (CAE) Algorithm

## Introduction

The Context-Aware Encryption (CAE) Algorithm is an innovative approach to data encryption that dynamically adjusts encryption keys based on a predefined set of environmental contexts. By integrating factors such as time, location, device status, and ambient conditions into the encryption process, CAE aims to enhance security measures beyond the capabilities of conventional encryption systems. This project seeks to offer a robust, adaptable encryption solution that responds to the changing conditions of its operational environment.

## Features

- **Dynamic Key Generation:** Generates encryption keys that adapt to changes in environmental context, making unauthorized decryption substantially more challenging.
- **Multi-Context Support:** Utilizes various contextual information (e.g., time, location, network status) to influence encryption, adding an extra layer of security.
- **Modular Design:** Facilitates easy integration into existing systems and applications, with minimal adjustments required.
- **Open Source:** Encourages community engagement, contribution, and improvement.

## Getting Started

### Prerequisites

- Python 3.6 or later
- Dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:
   
   ```bash
   git clone https://github.com/yourusername/CAE-Algorithm.git
   ```

2. Navigate to the project directory:
   
   ```bash
   cd CAE-Algorithm
   ```

3. Install the required dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```

##### Usage

This project provides two main functionalities: context-aware encryption and end-to-end (E2E) encryption. Below are the instructions on how to use each component.

### Context-Aware Encryption

The `context_encryption7.py` script demonstrates how to perform encryption operations that consider the context of the environment, such as the device usage, location frequency, and more, to dynamically generate a secure encryption key.

#### Basic Usage

1. **Import the Module:**

First, ensure you import the necessary function from the script:

```python
from context_encryption7 import simulate_encryption_process
```

2. **Simulate Encryption Process:**

To simulate the context-aware encryption process, simply call the function:

```python
simulate_encryption_process()
```

This function gathers contextual data, derives a secure key based on this data, encrypts a predefined plaintext message, and finally decrypts it to verify the process's integrity.

### End-to-End (E2E) Encryption

The `e2e_encryption.py` script illustrates how to perform end-to-end encryption using RSA for key exchange and AES for data encryption.

#### Generating RSA Key Pair

**Generate RSA Keys:**

First, import the function to generate an RSA key pair:

```python
from e2e_encryption import generate_rsa_key_pair
```

Then, generate your RSA key pair:

```python
private_pem, public_pem = generate_rsa_key_pair()
```

This will give you the private and public keys in PEM format.

#### Encrypting Data

**Encrypt Data:**

To encrypt data using the recipient's public key, use the `encrypt_data_with_e2e` function. Make sure to pass the data as a string and the public key in PEM format:

pythonCopy code

```python
from e2e_encryption import encrypt_data_with_e2e
data = "Sensitive information here."
encrypted_data, iv, encrypted_aes_key = encrypt_data_with_e2e(data, public_pem)
```

This function returns the encrypted data, the initialization vector (IV), and the AES key encrypted with the recipient's public RSA key.

---

**Note:** For a full understanding of how the encryption and decryption processes work and how to implement them in your applications, refer to the source code of `context_encryption7.py` and `e2e_encryption.py`. These examples are designed to get you started with the basic functionality of the CAE Algorithm project.

Ensure that you handle all cryptographic materials (e.g., keys) securely in your applications and adhere to best practices for cryptography to maintain the security and privacy of your data.

## Contributing

We welcome contributions from the community, whether it's in the form of bug reports, feature requests, or code contributions. For more information on how to contribute, please refer to the [CONTRIBUTING.md](https://github.com/mnarc123/CAE-Algorithm/blob/main/CONTRIBUTING.md) file.

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details.

## Acknowledgments

- Special thanks to all contributors who have helped to shape the CAE Algorithm.
- This project was inspired by ongoing research in dynamic encryption methods and context-aware security systems.

## Contact

For any queries or further discussions, please contact us via [GitHub Issues](https://github.com/mnarc123/CAE-Algorithm/issues).
