def encrypt(message, key):
    if len(key) != 4:
        print("The length of key should be of 4")
        return

    key = [[alphabets[key[0]],alphabets[key[1]]], [alphabets[key[2]],alphabets[key[3]]]]

    column_vector_generator = convertMessageToVectors(message)
    cipher = ''
    for each in column_vector_generator:
        cipher_vector = multiply(key, each)
        cipher += convertCipherVectorToText(cipher_vector)
    return cipher

def convertMessageToVectors(message):
    plain_text_column_vector = []
    for index, alpha in enumerate(message):
        if index % 2 == 0 and index != 0:
            yield plain_text_column_vector
            plain_text_column_vector = []
        plain_text_column_vector.append([alphabets[alpha]])

    yield plain_text_column_vector

def multiply(key, vector):
    resultant = [[0],[0]]
    for i in range(len(key)):
        for j in range(len(vector[0])):
            for l in range(len(vector)):
                resultant[i][j] += key[i][l] * vector[l][j]
                resultant[i][j] %= 26
    return resultant

def convertCipherVectorToText(vector):
   cipher = ''
   for i in range(len(vector)):
       for j in range(len(vector[0])):
           cipher += chr(vector[i][j]+65)
   return cipher


def decrypt():
    pass





if "__main__" == __name__:
    alphabets = {}
    for each in range(65, 91):
        alphabets[chr(each)] = each - 65

    print(encrypt('SHORTEXAMPLE', 'HILL'))
