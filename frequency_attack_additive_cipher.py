def predictPlainText(cipher):
    cipher_frequency = {}
    for each in cipher:
        if each in cipher_frequency.keys():
            cipher_frequency[each] += 1
        else:
            cipher_frequency[each] = 1
    totol_characters = len(cipher)

    for key, val in cipher_frequency.items():
        v = round((val/totol_characters)*100, 3)
        cipher_frequency[key] = v


    for _ in range(1,11):
        max_key_cipher = findMaxAndDelete(cipher_frequency)
        max_key = findMaxAndDelete(english_letter_frequency)
        shift = ord(max_key_cipher) - ord(max_key)
        print(f"{_}. The possible cipher can be \n", decrypt(cipher, shift).rstrip())

def decrypt(message, shift):
    '''~
    Decrypt the message
    :param message: The cipher text or encrypted message
    :param shift: The shift by which you want to decrypt the message
    :return: the decrypted message also known as original message
    '''
    original_message = ''
    for char in message:
        original_message += chr(((alphabets[char.upper()] - shift) % 26) + 65)
    return original_message

def findMaxAndDelete(dic):
    max = 0
    for key, val in dic.items():
        if max < val:
            max = val
            max_key = key.upper()
    del dic[max_key]
    return max_key


if "__main__" == __name__:
    english_letter_frequency = {
    "A": 8.167, "B": 1.492, "C": 2.782, "D": 4.253, "E":12.702 ,"F": 2.228, "G": 2.015, "H": 6.094, "I": 6.996, "J": 0.153, "K": 0.772, "L": 4.025, "M": 2.406, "N": 6.749, "O": 7.507, "P": 1.929, "Q": 0.095, "R": 5.987, "S": 6.327, "T": 9.056, "U": 2.758, "V": 0.978, "W": 2.360, "X": 0.150, "Y": 1.974, "Z": 0.074
    }
    alphabets = {}
    for each in range(65, 91):
        alphabets[chr(each)] = each - 65
    predictPlainText("OLIHLVRQHZRUGWKDWFRPHVZLWKPXOWLSOHPHDQLQJVDQGHASHULHQFHVDERYHDOOOLIHLVQRWMXVWDERXWHALVWHQFHEXWDOVRDERXWKRZDQLQGLYLGXDOGHILQHVWKDWHALVWHQFHKHQFHLWLVLPSRUWDQWWRORRNDWOLIHQRWMXVWIURPRQHVLQJOHSHUVSHFWLYHSKLORVRSKHUVVFKRODUVSRHWVDQGDXWKRUVKDYHZULWWHQPXFKDERXWZKDWFRQVWLWXWHVOLYLQJDQGPRUHLPSRUWDQWOBZKDWDUHWKHQHFHVVDUBLWHPVWKDWGHILQHVRPHRQHVOLIHRIFRXUVHWKLVHAHUFLVHKDVEHHQGRQHLQYDULRXVZDBVZKLOHSKLORVRSKHUVZRXOGWUBWRILQGWKHPHDQLQJDQGSXUSRVHEHKLQGWKHOLIHRILQGLYLGXDOVSRHWVDQGDXWKRUVZRXOGGRFXPHQWWKHULFKQHVVRIOLIHDWYDULRXVVWDJHVOLIHLVWKXVSHUKDSVVRPHWKLQJWKDWLVPRUHWKDQLQWULJXLQJ")