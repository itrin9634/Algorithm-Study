n = int(input())
a = 0
b = 0


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def findPrime(x):
    if x == 1:
        return False
    for j in range(3, x, 2):
        if isPrime(j) and isPrime(x - j):
            print('{0} = {1} + {2}'.format(x, j, x-j))
            return j


while n != 0:
    findPrime(n)
    n = int(input())
    if n == 0:
        break