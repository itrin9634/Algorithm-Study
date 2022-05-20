def check(n):
    i = 1
    d = 0
    while True:
        if i % n == 0:
            return len(str(i))
        else:
            d += 1
            i = (10 ** d) + i

while True:
    try:
        n = int(input())
        print(check(n))
    except:
        break