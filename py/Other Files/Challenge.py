#letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Old_Message = " "
New_Message = " "
def encrypt(Old_Message):
    Message['a'] = 'X'
    Message['b'] = 'Y'
    Message['c'] = 'Z'
    Message['d'] = 'B'
    Message['e'] = 'H'
    Message['f'] = 'R'
    Message['g'] = 'W'
    Message['h'] = 'P'
    Message['i'] = 'M'
    Message['j'] = 'O'
    Message['k'] = 'Q'
    Message['l'] = 'V'
    Message['m'] = 'I'
    Message['n'] = 'E'
    Message['o'] = 'C'
    Message['p'] = 'T'
    Message['q'] = 'S'
    Message['r'] = 'A'
    Message['t'] = 'D'
    Message['u'] = 'F'
    Message['v'] = 'J'
    Message['w'] = 'N'
    Message['x'] = 'G'
    Message['y'] = 'K'
    Message['z'] = 'L'

    Old_Message = Message
    return Old_Message

def Decrypt(New_Message):
    Old_Message['X'] = 'a'
    Old_Message['Y'] = 'b'
    Old_Message['Z'] = 'c'
    Old_Message['B'] = 'd'
    Old_Message['H'] = 'e'
    Old_Message['R'] = 'f'
    Old_Message['W'] = 'g'
    Old_Message['P'] = 'h'
    Old_Message['M'] = 'i'
    Old_Message['O'] = 'j'
    Old_Message['Q'] = 'k'
    Old_Message['V'] = 'l'
    Old_Message['I'] = 'm'
    Old_Message['E'] = 'n'
    Old_Message['C'] = 'o
    Old_Message['T'] = 'p'
    Old_Message['S'] = 'q'
    Old_Message['A'] = 'r'
    Old_Message['D'] = 's'
    Old_Message['F'] = 't'
    Old_Message['J'] = 'u'
    Old_Message['N'] = 'w'
    Old_Message['G'] = 'x'
    Old_Message['K'] = 'y'
    Old_Message['L'] = 'z'
    
    New_Message = Old_Message
    return New_Message

Message = input("Insert your message here: ")
print(encrypt(Message))

New = input("Do you want to decrypt it? (y/n): ")
 
if(New == "y"):
    decrypt()
elif(New == "n"):
    print("Good!")
else:
    print("Invalid response.")         
