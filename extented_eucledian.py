def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y

def extendedEucledian(a, b):

    x0  = 1
    y0 = 0

    x1 = 0
    y1 = 1

    rm2 = x0 * a + y0 * b
    rm1 = x1 * a + y1 *b

    r = None

    while(r != 0):
        q = rm2 // rm1

        r = a - q * b
        x = x0 - q * x1
        y = y0 - q * y1
        rm2 = rm1
        rm1 = r
        a = b
        b = r
        x0 = x1
        y0 = y1
        x1 = x
        y1 = y

    return rm2, x0 , y0


if "__main__" == __name__:
    print(gcdExtended(240, 46))
    print(extendedEucledian(240, 46))