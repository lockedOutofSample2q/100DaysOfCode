alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

new_alpha = []
text_to_encrypt= input("enter text: ").lower()
ceasar_num = input ("Choose the shifting amount: ")

def caesar_array(ceasar_num):
    for i in alphabet:
        new_alpha.append(alphabet[(alphabet.index(i)+int(ceasar_num))%26])
    return new_alpha

def ceasar_encrypt(text_to_encrypt, ceasar_num):
    new_alpha = caesar_array(ceasar_num)
    encrypted_text=""
    for i in text_to_encrypt:
        if i not in alphabet:
            encrypted_text = encrypted_text + i
        else:
            alphabet_index = alphabet.index(i)
            encrypted_text= encrypted_text + new_alpha[alphabet_index]
    print("Original text: " + text_to_encrypt)
    print("Encrypted text: " + encrypted_text)
    return encrypted_text

encrypted_text = ceasar_encrypt(text_to_encrypt, ceasar_num)

def ceasar_decrypt(encrypted_text, decryption_num):
    decrypted_text =""
    for i in encrypted_text:
        if i not in alphabet:
            decrypted_text = decrypted_text + i
        else:
            alphabet_index = alphabet.index(i)
            decrypted_text = decrypted_text + alphabet[alphabet_index - decryption_num]
    print("Decrypted text: " + decrypted_text)

decryption_num = input("Choose the decryption amount: ")

ceasar_decrypt(encrypted_text, int(decryption_num))
