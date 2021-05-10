alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n', 
            'o','p','q','r','s','t','u','v','w','x','y','z']

decode_encode = input("Do you want to encode a message or decode? ")
message = input("Please enter your message: )
shift_num = int(input("Enter shift number; "))

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