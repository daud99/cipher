def encrypt(message, shift):
    '''
    Encrypt the message
    :param message: The orginal text you wanted to encrypt
    :param shift: The shift by which you want to encrypt the message
    :return: the encrypted message also known as cipher
    '''
    cipher = ''
    for char in message:
        cipher += chr(((alphabets[char.upper()] + shift) % 26)+65)
    return cipher

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

if "__main__" == __name__:
    alphabets = {}
    for each in range(65, 91):
        alphabets[chr(each)] = each - 65
    # cipher = encrypt('meetmeafterthetogaparty', 3)
    cipher = encrypt('LifeisonewordthatcomeswithmultiplemeaningsandexperiencesAbovealllifeisnotjustaboutexistencebutalsoabouthowanindividualdefinesthatexistenceHenceitisimportanttolookatlifenotjustfromonesingleperspectivePhilosophersscholarspoetsandauthorshavewrittenmuchaboutwhatconstituteslivingandmoreimportantlywhatarethenecessaryitemsthatdefinesomeoneslifeOfcoursethisexercisehasbeendoneinvariouswaysWhilephilosopherswouldtrytofindthemeaningandpurposebehindthelifeofindividualspoetsandauthorswoulddocumenttherichnessoflifeatvariousstagesLifeisthusperhapssomethingthatismorethanintriguing', 3)
    print(f"Cipher is {cipher}")
    print(f"Plain is {decrypt(cipher, 3)}")


