logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n', 
            'o','p','q','r','s','t','u','v','w','x','y','z']

#taking input
decode_encode = input("Do you want to encode a message or decode? ")
message = input("Please enter your message: ")
shift_num = int(input("Enter shift number; "))

#encode function
def encode(message, shift_num):

    words = list(message.split(" "))

    encoded_words = []

    for word in words:
        encode_word1 = []
        char_en = list(word)

        for char in char_en:
            char = char.lower()
            if char in alphabet:
                index = alphabet.index(char)
                if index >= (26-shift_num):
                    index = index - (26 - shift_num)
                else:
                    index = index + shift_num
                
                encode_word1.append(alphabet[index])
            
            else:
                encode_word1.append(char)
        
        final_word = "".join(encode_word1)
        encoded_words.append(final_word)

    return " ".join(encoded_words)

#decode function
def decode(message, shift_num):
    
    words = list(message.split(" "))

    decoded_words = []

    for word in words:
        decode_word1 = []
        char_de = list(word)

        for char in char_de:
            char = char.lower()
            if char in alphabet:
                index = alphabet.index(char)
                if index <= (shift_num - 1):
                    index = index + (26-shift_num)
                else:
                    index = index - shift_num
                
                decode_word1.append(alphabet[index])
            
            else:
                decode_word1.append(char)
        
        final_word = "".join(decode_word1)
        decoded_words.append(final_word)
    
    return " ".join(decoded_words)


if decode_encode.lower() == "encode":
    print(encode(message, shift_num))

if decode_encode.lower() == "decode":
    print(decode(message, shift_num))