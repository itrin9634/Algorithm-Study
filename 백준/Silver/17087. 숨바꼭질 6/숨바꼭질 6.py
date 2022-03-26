n, s = map(int, input().split())
arr = list(map(int, input().split()))
array = []


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


for i in arr:
    array.append(abs(s-i))

result = array[0]

for i in range(1, n):
    result = gcd(result, array[i])
print(result)