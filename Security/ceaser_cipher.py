def caesar_encrypt(text, shift):
    result = ("")
    for char in text:
        # Check if the character is a letter (ignores numbers and punctuation)
        if char.isalpha():
            # Determine the ASCII offset: 65 for uppercase 'A', 97 for lowercase 'a'
            ascii_offset = 65 if char.isupper() else 97
            # Shift the character and wrap around using modulo 26
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)



def caeser_bruteforce(ciphered_text):
    for shift in range(26):
        print(f"attempting shift #{shift}: {caesar_encrypt(ciphered_text, -shift)}")
        #uses deshifting to attempt every possible caeser shift ^

ciphered_text = input("enter your text encrypted via caeser cipher")

caeser_bruteforce(ciphered_text)