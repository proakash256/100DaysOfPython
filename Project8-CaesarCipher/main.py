import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(art.logo)


def caesar(start_text, shift_number, cipher_direction):
    if cipher_direction == "decode":
        shift_number *= -1
    end_text = ""
    for i in start_text:
        if i.isalpha():
            end_text += alphabet[(alphabet.index(i) + shift_number) % len(alphabet)]
        else:
            end_text += i
    print(f"The {cipher_direction}d text is : {end_text}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_number=shift, cipher_direction=direction)
    ch = input("Type 'yes' to go again else 'no' : ")
    if ch == "no":
        print("GoodBye!!")
        break
