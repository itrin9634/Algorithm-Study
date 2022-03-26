n = int(input())


def gcd_sum(array):
    result = 0
    for i in range(1, len(array)):
        for j in range(i+1, len(array)):
            result += gcd(array[i], array[j])
    return result


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


for i in range(n):
    arr = list(map(int, input().split()))
    print(gcd_sum(arr))