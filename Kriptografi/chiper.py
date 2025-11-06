def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    
    return result

plaintext = "Hello World!"
shift = 3
encrypted = caesar_encrypt(plaintext, shift)
print(f"Original: {plaintext}")
print(f"Encrypted: {encrypted}")

     