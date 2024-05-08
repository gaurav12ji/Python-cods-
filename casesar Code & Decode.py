alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type Your message: \n").lower()
shift = int(input("Type the shift number \n"))


def encoded(en_text,en_shift):
    ch = ""
    for letter in en_text:
        position = alphabet.index(letter)
        new_positiopn = position+en_shift
        new_letter = alphabet[new_positiopn]
        ch += new_letter
    print(ch)
encoded(en_text=text,en_shift=shift)




