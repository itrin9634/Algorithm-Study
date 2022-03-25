num = int(input())
result = 1


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


result = factorial(num)
print(result)