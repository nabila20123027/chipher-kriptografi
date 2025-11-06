# === Hill Cipher ===
import numpy as np

def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace(" ", "")
    n = key_matrix.shape[0]
    while len(plaintext) % n != 0:
        plaintext += 'X'
    result = ""
    for i in range(0, len(plaintext), n):
        block = [ord(c) - 65 for c in plaintext[i:i+n]]
        encrypted = np.dot(key_matrix, block) % 26
        result += ''.join(chr(int(x) + 65) for x in encrypted)
    return result

def hill_decrypt(ciphertext, key_matrix):
    n = key_matrix.shape[0]
    det = int(round(np.linalg.det(key_matrix)))
    det_inv = pow(det % 26, -1, 26)
    adj = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    inv_matrix = (det_inv * adj) % 26

    result = ""
    for i in range(0, len(ciphertext), n):
        block = [ord(c) - 65 for c in ciphertext[i:i+n]]
        decrypted = np.dot(inv_matrix, block) % 26
        result += ''.join(chr(int(x) + 65) for x in decrypted)
    return result

# Contoh penggunaan
key_matrix = np.array([[3, 3], [2, 5]])
text = "HELLO"
encrypted = hill_encrypt(text, key_matrix)
decrypted = hill_decrypt(encrypted, key_matrix)

print("\n=== Hill Cipher ===")
print("Plaintext :", text)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)