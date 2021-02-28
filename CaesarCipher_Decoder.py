# Author: S Bryan

import sys
from collections import Counter
from langdetect import detect

print("----------Caesar Cipher Decoder----------")
filename = input("Enter .txt filename: ")
print()

# Open File
try:
    txt_file = open(filename, "r")
except IOError:
    print("Error - IOError")

# Read File
ciphertext = txt_file.read()
ciphertext = ciphertext.lower()
print("Ciphertext: ")
print(ciphertext)
print()

# Decode Ciphertext
alphabet = "abcdefghijklmnopqrstuvwxyz"
subAlphabet = {}


def createDict(shift):
    for i in range(0, 26):
        letter = alphabet[i]
        subAlphabet[letter] = alphabet[(i + shift) % 26]


def decodeCiphertext(cText, pText_list):
    pText = ""
    for letter in cText:
        if letter in subAlphabet:
            letter = subAlphabet[letter]
            pText = pText + letter
        elif letter == "\n":
            pText = pText + "\n"
        else:
            pText = pText + " "
    pText_list.append(pText)


plaintext_list = []
for i in range(0, 26):
    createDict(i)
    decodeCiphertext(ciphertext, plaintext_list)

plaintext = ""
detected = False;
for p in plaintext_list:
    if detect(p) == 'en':
        plaintext = p
        detected = True

if detected:
    print("Plaintext: ")
    print(plaintext)
else:
    print("Decoder failed to detect a plaintext")
    print("Possible Plaintext: ")
    print(plaintext_list)



