for _ in range(int(input())):
    num, s = map(str, input().split())
    arr = list(s)
    for a in arr:
        print(a * int(num), end='')
    print()