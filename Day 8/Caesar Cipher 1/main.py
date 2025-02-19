def main():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
    #  message.
    encrypt(text, alphabet, shift)


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, alphabet, shift):
    encrypted_text_list = []
    encrypted_text = ''
    for letter_one in original_text:
        for letter_two in alphabet:
            if letter_one == letter_two:
                index = alphabet.index(letter_two) + shift
                # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
                if index > len(alphabet):
                    index -= len(alphabet)

                encrypted_text_list.append(alphabet[index])

    for encrypted_letter in encrypted_text_list:
        encrypted_text += encrypted_letter

    # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
    #  by the shift amount and print the encrypted text.
    print(encrypted_text)


main()

