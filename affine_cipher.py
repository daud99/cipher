def findGCD(n1, n2):
    while(n2 != 0):
        if n1 > n2:
            n1 , n2 = n2, n1 % n2
        else:
            n1, n2 = n1, n2 % n1
    return n1


def modInverse(a, m):
    m0 = m
    y = 0
    x = 1

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

def encrypt(alpha, beta, plaintext):
    cipher = ''
    if findGCD(alpha, 26) != 1:
        return "Invalid alpha"
    if not(beta >= 0 and beta <= 25):
        return "invalid beta"
    for alphabet in plaintext:
        cipher += chr((((alphabets[alphabet.upper()]* alpha) + beta) % 26) + 65)
    return cipher

def decrypt(alpha, beta, cipher):
    plain = ""
    for alphabet in cipher:
        plain += chr((((alphabets[alphabet.upper()] - beta) * modInverse(alpha, 26)) % 26) + 65)
    return plain

if "__main__" == __name__:
    alphabets = {}
    for each in range(65, 91):
        alphabets[chr(each)] = each - 65
    e = encrypt(5,5,"MYNAMEISDAUD")
    print(e)
    d = decrypt(5, 5, e)
    print(d)