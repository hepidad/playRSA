# do_encrypt.py
# Encrypt a plaintext file using RSA public key

import argparse
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

def load_public_key(path):
    with open(path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())
    return public_key

def encrypt_text(plaintext: bytes, public_key) -> bytes:
    ciphertext = public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def main():
    parser = argparse.ArgumentParser(description="Encrypt a file using RSA public key.")
    parser.add_argument("-i", "--input", required=True, help="Input plaintext file")
    parser.add_argument("-o", "--output", required=True, help="Output ciphertext file")
    parser.add_argument("-pubkey", "--public_key", required=True, help="Public key file (PEM)")

    args = parser.parse_args()

    # Read input plaintext
    with open(args.input, "rb") as f:
        plaintext = f.read()

    # Load public key
    public_key = load_public_key(args.public_key)

    # Encrypt
    encrypted_bytes = encrypt_text(plaintext, public_key)

    # Save encrypted text (Base64 encoded)
    with open(args.output, "wb") as f:
        f.write(base64.b64encode(encrypted_bytes))

    print(f"Encryption complete. Ciphertext saved to: {args.output}")

if __name__ == "__main__":
    main()
