num = int(input())


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


fac = factorial(num)
count = 0

while fac > 10:
    if fac % 10 == 0:
        count += 1
        fac //= 10
    else:
        break
print(count)
