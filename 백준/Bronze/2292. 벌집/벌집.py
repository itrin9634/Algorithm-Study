n = int(input())
answer = 1
cur = 1
plus = 6
if n == 1:
    answer = 1
    print(answer)
else:
    while True:
        cur += plus
        answer += 1
        if n <= cur:
            print(answer)
            break
            exit(0)
        plus += 6
