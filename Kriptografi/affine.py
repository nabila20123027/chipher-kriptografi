# Affine Cipher Implementation in Python

def gcd(a, b):
    """Menghitung FPB (Faktor Persekutuan Terbesar)"""
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Mencari invers modular dari a terhadap m"""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(text, a, b):
    """Fungsi enkripsi Affine Cipher"""
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            x = ord(char) - base
            result += chr(((a * x + b) % 26) + base)
        else:
            result += char
    return result

def affine_decrypt(cipher, a, b):
    """Fungsi dekripsi Affine Cipher"""
    result = ""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Tidak ada invers modular untuk nilai a ini. Pilih a lain (yang relatif prima dengan 26)."
    
    for char in cipher:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            y = ord(char) - base
            result += chr(((a_inv * (y - b)) % 26) + base)
        else:
            result += char
    return result


# ======== Program Utama ========

plaintext = input("Masukkan teks yang ingin dienkripsi: ")
a = int(input("Masukkan nilai a (relatif prima dengan 26, contoh: 5, 7, 11, 17, 25): "))
b = int(input("Masukkan nilai b (0–25): "))

# Validasi nilai a
if gcd(a, 26) != 1:
    print("❌ Nilai a tidak valid! Harus relatif prima dengan 26.")
else:
    encrypted = affine_encrypt(plaintext, a, b)
    decrypted = affine_decrypt(encrypted, a, b)

    print("\n=== HASIL ===")
    print(f"Plaintext : {plaintext}")
    print(f"Encrypted : {encrypted}")
    print(f"Decrypted : {decrypted}")
