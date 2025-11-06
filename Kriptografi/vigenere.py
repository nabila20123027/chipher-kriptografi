import sys
from colorama import init, Fore


# Initialise colorama
init()

def vigenere_encrypt(plain_text, key):
    encrypted_text = ''
    key_repeated = (key * (len(plain_text) // len(key))) + key[:len(plain_text) % len (key)]
    for i in range(len(plain_text)):
        if plain_text [i].isalpha():
            shift = ord(key_repeated[i].upper()) -ord('A')
            if plain_text[i].isupper():
                encrypted_text +=chr((ord(plain_text[i]) + shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_text +=chr((ord(plain_text[i]) + shift - ord('a')) % 26 + ord('a'))
        else:
            encrypted_text += plain_text[i]
    return encrypted_text
def vigenere_decrypt(chiper_text, key):
    decryted_text = ''
    key_repeated = (key * (len(chiper_text) // len (key))) + key[:len(chiper_text) % len(key)]
    for i in range(len(chiper_text)):
        if chiper_text[i].isalpha():
            shift = ord(key_repeated[i].upper()) - ord('A')
            if chiper_text[i].isupper():
                decryted_text += chr((ord(chiper_text[i]) - shift - ord('A')) % 26 + ord('A'))
            else: 
                decryted_text += chr((ord(chiper_text[i]) - shift - ord('a')) % 26 + ord('a'))
        else:
            decryted_text += chiper_text[i]
            
    return decryted_text           

key = "KEY"
# Get user input (Message to encrypt).
plaintext = input('[!] Enter your message: ')
# Encrypt the plaintext using the Vigenère cipher
cipher_text = vigenere_encrypt(plaintext, key)
# Print the results
print(f"[+] Plaintext: {plaintext}")
print(f"{Fore.GREEN}[+] Ciphertext: {cipher_text}")
# Ask if user wants to decrypt the message (just to see the functionality.)
ask_to_decrypt = input('\n\n[?] Do you want to decrypt the message?\n[?] Y or N: ').lower()
# If user wants to.
if ask_to_decrypt == 'y':
   # Decrypt the ciphertext back to the original plaintext.
   decrypted_text = vigenere_decrypt(cipher_text, key)
   print(f"{Fore.GREEN}[+] Decrypted text: {decrypted_text}")
# If user does not want to.
elif ask_to_decrypt == 'n':
   sys.exit()
# When an invalid input is entered.
else:
   print(f"{Fore.RED}[-] Invalid input.")  