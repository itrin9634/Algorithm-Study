e, s, m = map(int, input().split())
result = 1
while True:
    if (result - e) %15 == 0 and (result - s) % 28 == 0 and (result-m) % 19 == 0:
        print(result)
        break
    else:
        result += 1
