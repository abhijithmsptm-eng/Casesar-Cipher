alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def ceaser(orgianl_text, shifted_number, encode_or_decode):
    output_text = "" 
    for letter in orginal_text:
        if letter not in alphabet:
            output_text += letter
        else:
            if encode_or_decode == "decode":
                shifted_number *= -1

                shifted_position = alphabet.index(letter) + shifted_number
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
        
        print(f"Here is the {encode_or_decode}d test result: {output_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n ").lower()
    text = input("Enter youre message:  \n").lower()
    shift = int(input("Enter the shift number: \n"))

    ceaser(orgianl_text=text, shifted_number=shift, encode_or_decode=direction)

    restart = input("type 'yes' if you want to continue, otherwise type 'no'. \n").lower()

    if restart == "no":
        should_continue = False

        print("Good bie")