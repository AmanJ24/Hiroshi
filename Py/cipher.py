logo = '''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88  
'''
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
#Creating the function to encrypt and decrypt. 
def caeser(plain_text, shift_amount):
    cipher_text = ""
    if direction == 'encode':
        for letter in plain_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:
                cipher_text += letter
        print(f"The encoded text is {cipher_text}")     #Now printing the encoded text.
    elif direction == 'decode':
        for letter in plain_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - shift_amount
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:
                cipher_text = letter
        print(f"The decoded text is {cipher_text}")      #Now printing the decoded text.
    else:
        print("Invalid text.")                           #This is to tell the user that the text is not valid.

should_continue = True
while should_continue:
    #Now taking input from the user. 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26                                     #This is to limit the maximum shift to 26 
    caeser(plain_text = text, shift_amount = shift)        #This is to call to function.

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye!")        