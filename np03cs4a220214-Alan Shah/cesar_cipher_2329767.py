# AlanShah
# np03cs4a220214-Alan Shahn
def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_char = chr((ord(char) + shift - 97) % 26 + 97)
            ciphertext += shift_char
        else:
            ciphertext += char
    return ciphertext
def decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_char = chr((ord(char) - shift - 97) % 26 + 97)
            plaintext += shift_char
        else:
            plaintext += char
    return plaintext
    
def main():
    while True:
        mode = input("Select a mode (encrypt/decrypt): ").lower()
        while mode != "encrypt" and mode != "decrypt":
            mode = input("Invalid mode. Please select a valid mode (encrypt/decrypt): ").lower()
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (1-26): "))
        while shift < 1 or shift > 26:
            shift = int(input("Invalid shift value. Please enter a value between 1 and 26: "))
        if mode == "encrypt":
            output = encrypt(message, shift)
            print("Encrypted message:", output)
        else:
            output = decrypt(message, shift)
            print("Decrypted message:", output)
        again = input("Do you want to encrypt/decrypt another message? (y/n): ").lower()
        while again != "y" and again != "n":
            again = input("Invalid input. Please enter y or n: ").lower()
        if again == "n":
            break
if __name__ == "__main__":
    main()
