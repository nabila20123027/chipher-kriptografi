# TUGAS 2 - KRIPTOGRAFI
# Implementasi Algoritma Modern: RSA + Digital Signature
# Kelompok: Nabilla Maesaroh (20123027) & Sayyidah Muthi Nur Aisyah (20123003)


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pss
from Crypto.Hash import SHA256
import base64, os

# Tahap 1: Generate RSA Key Pair (2048-bit) & Simpan File
def generate_rsa_keys(bits=2048, priv_file="private.pem", pub_file="public.pem", passphrase=None):
    key = RSA.generate(bits)
    if passphrase:
        priv_pem = key.export_key(passphrase=passphrase, pkcs=8, protection="scryptAndAES128-CBC")
    else:
        priv_pem = key.export_key()
    pub_pem = key.publickey().export_key()
    with open(priv_file, "wb") as f:
        f.write(priv_pem)
    with open(pub_file, "wb") as f:
        f.write(pub_pem)
    print(f"Generated RSA-{bits} keys and saved to {priv_file}, {pub_file}")
    return priv_pem, pub_pem

# Tahap 2: Enkripsi dan Dekripsi (OAEP)
def rsa_encrypt(pub_pem: bytes, plaintext: bytes) -> str:
    pub = RSA.import_key(pub_pem)
    cipher = PKCS1_OAEP.new(pub)
    ciphertext = cipher.encrypt(plaintext)
    return base64.b64encode(ciphertext).decode()

def rsa_decrypt(priv_pem: bytes, b64_ciphertext: str) -> bytes:
    priv = RSA.import_key(priv_pem)
    cipher = PKCS1_OAEP.new(priv)
    ciphertext = base64.b64decode(b64_ciphertext)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Tahap 3: Digital Signature (PSS)
def sign_pss(priv_pem: bytes, data: bytes) -> str:
    priv = RSA.import_key(priv_pem)
    h = SHA256.new(data=data)
    signer = pss.new(priv)
    signature = signer.sign(h)
    return base64.b64encode(signature).decode()

def verify_pss(pub_pem: bytes, data: bytes, b64_signature: str) -> bool:
    pub = RSA.import_key(pub_pem)
    h = SHA256.new(data=data)
    signature = base64.b64decode(b64_signature)
    verifier = pss.new(pub)
    try:
        verifier.verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

# Tahap 4: Program Utama
def main():
    # Generate keypair
    priv_pem, pub_pem = generate_rsa_keys(2048)

    # Pesan yang akan dienkripsi
    message = b"Hello Cryptography - Nabilla & Muthi"

    # Enkripsi pesan
    ct_b64 = rsa_encrypt(pub_pem, message)
    print("\nCiphertext (base64):", ct_b64[:80], "...")

    # Dekripsi pesan
    pt = rsa_decrypt(priv_pem, ct_b64)
    print("Decrypted message:", pt.decode())

    # Buat signature
    sig_b64 = sign_pss(priv_pem, message)
    print("\nSignature (base64):", sig_b64[:80], "...")

    # Verifikasi signature
    verify_original = verify_pss(pub_pem, message, sig_b64)
    verify_tampered = verify_pss(pub_pem, message + b'.', sig_b64)

    print("\nVerify (original message):", verify_original)
    print("Verify (tampered message):", verify_tampered)

    # Tahap 5: Simpan hasil ke file
    with open("ciphertext.txt", "w") as f:
        f.write(ct_b64)
    with open("signature.txt", "w") as f:
        f.write(sig_b64)
    print("\nSaved: private.pem, public.pem, ciphertext.txt, signature.txt")

# Jalankan program utama
if __name__ == "__main__":
    main()