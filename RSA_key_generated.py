# RSA_key_generated.py
# Demonstrates RSA private/public key generation using the cryptography library

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os

def generate_rsa_keys(key_size=2048, output_dir="keys"):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size
    )

    # Derive public key
    public_key = private_key.public_key()

    # Serialize and save the private key
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open(os.path.join(output_dir, "private_key.pem"), "wb") as f:
        f.write(private_pem)

    # Serialize and save the public key
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(os.path.join(output_dir, "public_key.pem"), "wb") as f:
        f.write(public_pem)

    print(f"RSA keys (size: {key_size}) have been generated and saved to '{output_dir}/'.")

if __name__ == "__main__":
    generate_rsa_keys()
