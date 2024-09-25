'''
#How It Works:
The script allows us to choose between encryption or decryption:

#Encryption:
Enter the text wish to encrypt.
Provide a numerical key for the shift.
The program then shifts each letter by the key value and returns the encrypted result.

#Decryption:
Input the ciphertext and key.
The program reverses the process by shifting the letters in the opposite direction.

'''

alphabets = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        letter = letter.lower()
        if letter in alphabets:
            index = alphabets.find(letter)
            new_index = (index + key) % 26
            ciphertext += alphabets[new_index]
        else:
            ciphertext += letter
    return ciphertext
    
def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        letter=letter.lower()
        if letter in alphabets:
            index = alphabets.find(letter)
            new_index = (index - key) % 26
            plaintext += alphabets[new_index]
        else:
                plaintext += letter
    return plaintext

choice = input("Enter e for encryption and d for decryption: ")

if (choice == "e"):
    plaintext = input("Enter plaintext value: ")
    key = int(input("Enter key value: "))
    ciphertext = encrypt(plaintext, key)
    print("Encrypted text: ", ciphertext)

elif (choice == "d"):
    ciphertext = input("Enter ciphertext value: ")
    key = int(input("Enter key value: "))
    plaintext = decrypt(ciphertext, key)
    print("Decrypted text: ", plaintext)
    
else:
    print("Enter a valid input")
