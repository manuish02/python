import math
def isPrime(n) :
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
    if (n % 2 == 0 or n % 3 == 0 ) :
        return False
    max_div = int(math.sqrt(n))
    for i in range(5, 1 + max_div):
        if n % i == 0:
            return False
    return True
def sillyGame(n):
    m = []
    primenumbers = []
    for i in range(1, n+1):
        if isPrime(i):
            primenumbers.append(i)
    if len(primenumbers) % 2 == 0:
        return 'Bob'
    else:
        return 'Alice'
    #
print(sillyGame(3))
print(sillyGame(6))
