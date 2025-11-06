# === Playfair Cipher ===
def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    for char in key:
        if char not in matrix and char.isalpha():
            matrix.append(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in matrix:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j

def playfair_encrypt(text, key):
    matrix = generate_key_matrix(key)
    text = text.upper().replace("J", "I")
    prepared = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = 'X' if (i + 1 == len(text) or text[i+1] == a) else text[i+1]
        prepared += a + b
        i += 2 if b != 'X' else 1

    result = ""
    for i in range(0, len(prepared), 2):
        a, b = prepared[i], prepared[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            result += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            result += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    return result

def playfair_decrypt(ciphertext, key):
    matrix = generate_key_matrix(key)
    result = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            result += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1 == col2:
            result += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    return result

# Contoh penggunaan
key = "MONARCHY"
text = "INSTRUMENTS"
encrypted = playfair_encrypt(text, key)
decrypted = playfair_decrypt(encrypted, key)

print("\n=== Playfair Cipher ===")
print("Plaintext :", text)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)