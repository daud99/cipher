def encrypt(message, key):
    if len(key) != 4:
        print("The length of key should be of 4")
        return

    key = [[alphabets[key[0]], alphabets[key[1]]], [alphabets[key[2]], alphabets[key[3]]]]

    column_vector_generator = convertMessageToVectors(message)
    cipher = ''
    for each in column_vector_generator:
        cipher_vector = multiply(key, each)
        cipher += convertVectorToText(cipher_vector)
    return cipher

def convertMessageToVectors(message):
    column_vector = []
    for index, alpha in enumerate(message):
        if index % 2 == 0 and index != 0:
            yield column_vector
            column_vector = []
        column_vector.append([alphabets[alpha]])

    yield column_vector

def multiply(key, vector):
    resultant = [[0],[0]]
    for i in range(len(key)):
        for j in range(len(vector[0])):
            for l in range(len(vector)):
                resultant[i][j] += key[i][l] * vector[l][j]
                resultant[i][j] %= 26
    return resultant

def convertVectorToText(vector):
   text = ''
   for i in range(len(vector)):
       for j in range(len(vector[0])):
           text += chr(vector[i][j]+65)
   return text

def modInverse(a, m):
    m0 = m
    y = 0
    x = 1

    # For (n mod 1) for any n will always be equal to zero
    if (m == 1):
        return 0

    while (a > 1):
        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if (x < 0):
        x = x + m0

    return x

def decrypt(cipher, key):
    key = [[alphabets[key[0]], alphabets[key[1]]], [alphabets[key[2]], alphabets[key[3]]]]
    determinant = ((key[0][0] * key[1][1]) - (key[0][1] * key[1][0]))
    key[0][0], key[1][1], key[0][1], key[1][0] = key[1][1] % 26, key[0][0] % 26, (key[0][1] * -1)%26, (key[1][0] * -1)%26
    determinant = determinant % 26
    determinant = modInverse(determinant, 26)
    for i in range(len(key)):
        for j in range(len(key[0])):
                key[i][j] *= determinant
    vectors = convertMessageToVectors(cipher)
    plain_text = ''
    for vector in vectors:
        plain_vector = multiply(key, vector)
        for i in range(len(plain_vector)):
            for j in range(len(plain_vector[0])):
                plain_text += chr(((int(plain_vector[i][j])%26))+65)
    return plain_text


if "__main__" == __name__:
    alphabets = {}
    for each in range(65, 91):
        alphabets[chr(each)] = each - 65
    cipher = encrypt('DAUDAHMEDD', 'HILL')
    print(f'The cipher for the given text DAUDAHMEDD is {cipher}')
    text = decrypt(cipher, 'HILL')
    print(f'The plaintext for the given text {cipher} is {text}')