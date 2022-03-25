n = int(input())


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


for i in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))
