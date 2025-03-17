#caesar_cipher in cryptography

#Encryption


#Alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '] 

#plain_text = input(str("What is the plain text you wish to encrypt: "))

#shift = int(input("What is the shift you wish to use: "))

plain_text = ""
shift = ""
cipher_text = ""


#Encrypt function
def encrypt(plain_text,shift):
    plain_text = input(str("What is the plain text you wish to encrypt: "))
    shift = int(input("What is the shift you wish to use: "))
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position +shift
        if new_position > 25:
            new_position2 = new_position-26
            new_letter2 = alphabet[new_position2]
            cipher_text += new_letter2
        else:
            new_letter1 = alphabet[new_position]
            cipher_text += new_letter1
    print(f"the encoded text is {cipher_text}")
    


#Decrypt function
def decrypt(cipher_text, shift):
  cipher_text = input(str("What is the ciphertext you wish to decrypt: ")).lower()
  shift = int(input("What is the shift you wish to use: "))
  plain_text = ""
  space = " "
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = int(position) - int(shift)
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")


mode = input("Do you want to Encrypt or Decrypt (E/D): ")

if mode == "E":
    encrypt(plain_text= plain_text,shift = shift)
elif mode == "D":
    decrypt(cipher_text, shift)
else:
    exit()
