def findMaxAndDelete(dic):
    max = 0
    for key, val in dic.items():
        if max < val:
            max = val
            max_key = key.upper()
    del dic[max_key]
    return max_key

def predictPlainText(cipher):
    cipher_frequency = {}
    for each in cipher:
        if each in cipher_frequency.keys():
            cipher_frequency[each.upper()] += 1
        else:
            cipher_frequency[each.upper()] = 1
    totol_characters = len(cipher)

    for key, val in cipher_frequency.items():
        v = round((val/totol_characters)*100, 3)
        cipher_frequency[key] = v

    for _ in range(len(cipher_frequency.keys())):
        cipher_max = findMaxAndDelete(cipher_frequency)
        lang_max = findMaxAndDelete(english_letter_frequency)
        cipher = cipher.upper().replace(cipher_max, lang_max)
    return cipher


def decrypt(message):
    plain_text = ""
    for alphabet in message:
        plain_text += reverse_key[alphabet.upper()]
    return plain_text


def encrypt(message):
    cipher = ""
    for alphabet in message:
        cipher += key[alphabet.upper()]
    return cipher


if "__main__" == __name__:
    key = {
    "A": "Y", "B": "C", "C": "G", "D": "F", "E": "D" ,"F": "Q", "G": "R", "H": "S", "I": "T", "J": "U", "K": "W", "L": "V", "M": "X", "N": "E", "O": "Z", "P": "M", "Q": "B", "R": "P", "S": "H", "T": "I", "U": "J", "V": "L", "W": "K", "X": "N", "Y": "A", "Z": "O"
    }
    english_letter_frequency = {
        "A": 8.167, "B": 1.492, "C": 2.782, "D": 4.253, "E": 12.702, "F": 2.228, "G": 2.015, "H": 6.094, "I": 6.996,
        "J": 0.153, "K": 0.772, "L": 4.025, "M": 2.406, "N": 6.749, "O": 7.507, "P": 1.929, "Q": 0.095, "R": 5.987,
        "S": 6.327, "T": 9.056, "U": 2.758, "V": 0.978, "W": 2.360, "X": 0.150, "Y": 1.974, "Z": 0.074
    }
    reverse_key = {y:x for x,y in key.items()}


    print(encrypt("wearegoingtobombdelhisaturday"))
    print(decrypt(encrypt("wearegoingtobombdelhisaturday")))
    print("The predicted text using frequency analysis is below")
    print(predictPlainText("wearegoingtobombdelhisaturday"))