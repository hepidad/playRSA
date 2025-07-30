# 🔐 RSA Encryption & Decryption with Python (playmode ON) 

This repository provides basic tools to demonstrate **RSA public-key cryptography** using Python and the [`cryptography`](https://cryptography.io/en/latest/) library.

You can:
- Generate public/private key pairs.
- Encrypt a plaintext file using a public key.
- Decrypt it back using the private key.


## 📦 Requirements

Install the required Python package:

```bash
pip install cryptography
```


# How to play this game?

This section explains, step-by-step, how to use the RSA encryption and decryption scripts in this project — designed for beginner-level computer science students learning cryptography.

---

## 🔹 Step 1: What Is Plain Text?

**Plain text** is a normal, readable message. For example:

```bash
Meet me at 5 PM near the library.
```
We call this **"plain text"** because it's not hidden or protected in any way.


## 🔹 Step 2: Why Do We Encrypt?

We encrypt messages to **protect them** from being read by anyone except the intended recipient.

Encryption turns **plain text** into **cipher text** — a scrambled, unreadable format that looks like random letters and numbers.


## 🔹 Step 3: What Is a Public Key?

Great question! 🔑

In public-key cryptography (like RSA), we use two keys:

- A **public key**: This can be shared with everyone — even strangers.
- A **private key**: This is kept secret and never shared.

To send a secure message:
- You **encrypt** the message using the **recipient's public key**.
- Only the person with the **matching private key** can **decrypt** and read the message.

> 💡 Think of the public key like a locked mailbox:  
> Anyone can drop a message inside, but only the owner with the private key can open it.


This script creates a 2048-bit RSA key pair and saves them to a keys/ directory.
```bash
python3 RSA_key_generated.py
```
🔧 Output:
- keys/public_key.pem – Public key
- keys/private_key.pem – Private key

> 💡 Remember, this key is pairing.   

## 🔹 Step 4: How to Encrypt a File

1. First, create a text file with a message:
```bash
echo "This is a secret mission." > message.txt
```

2. Then, encrypt the file using the recipient's public key:
```bash
python3 do_encrypt.py -i message.txt -o encrypted.txt -pubkey keys/public_key.pem
```
- -i = input (plain text file)
- -o = output (cipher text file)
- -pubkey = path to the recipient’s public key (for the sake of example, we can use public key that we've create before)

## 🔹 Step 5: How to Decrypt It
Only the person with the matching private key can unlock the message.
```bash
python3 do_decrypt.py -i encrypted.txt -o decrypted.txt -privkey keys/private_key.pem
```
- -i = input (cipher text file)
- -o = output (decrypted plain text)
- -privkey = path to your private key

Now, decrypted.txt will contain the original message.

## 🧠 Summary
- ✍️ Plain text = your original message
- 🔒 Cipher text = encrypted message
- 🔑 Public key = used to encrypt (can be shared)
- 🔐 Private key = used to decrypt (must be secret)

This is the foundation of secure communication on the internet — used in messaging apps, banking, websites (HTTPS), and more.

Happy encrypting! 🔐✨

