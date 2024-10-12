# A dictionary for International Morse Code
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# ask the user to input the message that requires morse encoding
keyword = input('Type your message here: \n')

# A function to encode the user input message to morse code
def morse_encoder(word: str):
    morse_code = []
    for char in word.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append(" ")
    return morse_code

morse_code_output = morse_encoder(keyword)

# a function to decode the encrypted morse code
def morse_decoder(encrypted_message: list):
    key_list = list(MORSE_CODE_DICT.keys())
    values_list = list(MORSE_CODE_DICT.values())
    decoded_code = ""
    symbol_text = ""

    for symbol in encrypted_message:
        print(symbol)
        try:
            code_idx = values_list.index(symbol)
            decoded_code += key_list[code_idx]
        except ValueError:
            decoded_code += symbol
    print(decoded_code)

    return decoded_code.title()

morse_decoded =  morse_decoder(morse_code_output)


morse_code_output_str = "".join(morse_code_output)
print(f"The morse code for your message '{keyword}' is : {morse_code_output_str} ")
print(f"The decoded message: {morse_decoded}")

