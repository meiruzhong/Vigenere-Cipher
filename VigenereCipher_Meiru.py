# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 18:18:13 2022

@author: Meiru
"""
# define a function to check if the key is valid.
# Here, being valid means the key only contains letters
def is_valid(text):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for value in text:
        if letters.find(value) == -1:
            return False
    return True

# input a message that want to be encrpted
plaintext = input('Please enter a message: ').lower()
print('Plaintext: ' + plaintext)

# input a key as a hint
key = input('Please enter a key: ')
print('Key: ' + key)
while is_valid(key) != True:
    print("please enter a valid key with letters only")
    key = input("Please enter a valid key: ")

# input shift to increase the difficulty to be deciphered
shift = int(input('Please enter a shift? '))

# make sure the length of the key is the same as that of the plaintext
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
len_letters = len(letters)
len_numbers = len(numbers)
key = key * int(len(plaintext)//len(key)+1)
key = key[:len(plaintext)]
print("The final key is: "+key)

# encrpted a plaintext 
encrypted = ''

for character in plaintext:
    
    index_letter = letters.find(character)
    index_number = numbers.find(character)

    if index_letter > -1:
        encrypted += letters[(index_letter + shift) % len_letters]

    elif index_number > -1:
        encrypted += numbers[(index_number + shift) % len_numbers]

    else:
        encrypted += character

print('Encrypted: ' + encrypted)

# decrypted the hidden message
decrypted = ''
for character in encrypted:
    index_letter = letters.find(character)
    index_number = numbers.find(character)
    if index_letter > -1:
        decrypted += letters[index_letter - (shift % len_letters)]
    elif index_number > -1:
        decrypted += numbers[index_number - (shift % len_numbers)]
    else:
        decrypted += character

print('Decrypted: ' + decrypted)

# verify if the decrpted message is the same as the plaintext
if decrypted == plaintext:
    print('All good, decrypted is same as the plaintext.')
else:
    print('Something is wrong, decrypted is not the same as the plaintext.')
