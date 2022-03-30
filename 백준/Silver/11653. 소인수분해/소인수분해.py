n = int(input())
i = 2

if n == 1:
    print()
else:
    while i <= n:
        if n % i == 0:
            print(i)
            n //= i
            i = 2
        else:
            i += 1