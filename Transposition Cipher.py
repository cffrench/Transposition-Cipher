# Connor Ffrench
# 11 April 2021
# Project 1
# This program implements a Transposition Cipher 

from functools import reduce

# Generates and returns the key used in the transposition cipher.  
# This will include a random permutation of the alphabet.   The data structure is your design. 
def key_gen():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters_to_assign = []
    for i in range len(letters):
        letters_to_assign.append(letters[i])
    key = []
    for j in range len(letters_to_assign):
        chosen_position = randint(len(letters_to_assign))
        key.append(letters_to_assign[chosen_position])
        
    return key

# Returns the encryption of string, plain_txt,  using a permuted alphabet which is part of 
# key and the transposition cipher.  Again, the data structure used for key is up to you. 
def encrypt(plaintext, key):

    return cipher_text

# Returns the decryption of string, cipher_txt,  using a permuted alphabet which is part of 
# key and the transposition cipher.  Again, the data structure used for key is up to you. 
def decrypt(cipher_txt, key):
    
    return decoded_text

def main():
    plaintext = "HELLO WORLD"
    key = key_gen()
    cipher_text = encrypt(plaintext, key)
    decoded_text = decrypt(cipher_txt, key)
    
main()