
def sillyGame(n):
    m = [True for i in range(n+1)]
    m[0] = False
    m[1] = False
    j = 2
    while( j * j <= n):
        if (m[j] == True):
            for i in range(j * j, n + 1 , j):
                m[i] = False
        j += 1
    if m.count(True) % 2 == 0:
        return 'Bob'
    else:
        return 'Alice'
    #
print(sillyGame(3))
print(sillyGame(6))
