# do_decrypt.py
# Decrypt a ciphertext file using RSA private key

import argparse
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

def load_private_key(path):
    with open(path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)
    return private_key

def decrypt_text(ciphertext_b64: bytes, private_key) -> bytes:
    ciphertext = base64.b64decode(ciphertext_b64)
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext

def main():
    parser = argparse.ArgumentParser(description="Decrypt a file using RSA private key.")
    parser.add_argument("-i", "--input", required=True, help="Input ciphertext file (Base64)")
    parser.add_argument("-o", "--output", required=True, help="Output plaintext file")
    parser.add_argument("-privkey", "--private_key", required=True, help="Private key file (PEM)")

    args = parser.parse_args()

    # Read encrypted input
    with open(args.input, "rb") as f:
        encrypted_data = f.read()

    # Load private key
    private_key = load_private_key(args.private_key)

    # Decrypt
    try:
        plaintext = decrypt_text(encrypted_data, private_key)
    except Exception as e:
        print("Decryption failed:", str(e))
        return

    # Save output
    with open(args.output, "wb") as f:
        f.write(plaintext)

    print(f"Decryption complete. Plaintext saved to: {args.output}")

if __name__ == "__main__":
    main()
