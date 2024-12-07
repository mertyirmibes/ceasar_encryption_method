# ceasar encryption system
def encrypt(text):
    encrypted_text = ""
    for letter in text:
        ascii_code = ord(letter)
        ascii_code = ascii_code + 3
        char_code = chr(ascii_code)
        encrypted_text += char_code

    print("Encrypted text: " + encrypted_text)
    return encrypted_text


def decrypt(encrypted_text):
    decrypted_text = ""
    for letter in encrypted_text:
        ascii_code = ord(letter)
        ascii_code = ascii_code - 3
        char_code = chr(ascii_code)
        decrypted_text += char_code

    print("Decrypted text: " + decrypted_text)
    return decrypted_text


# Loop until user enters 'stop'
while True:
    choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'stop' to exit: ").lower()

    if choice == "stop":
        print("Program terminated.")
        break
    elif choice == "e":
        text = input("Enter text to encrypt: ")
        encrypted = encrypt(text)
    elif choice == "d":
        encrypted_text = input("Enter text to decrypt: ")
        decrypt(encrypted_text)
    else:
        print("Invalid choice. Please try again.")