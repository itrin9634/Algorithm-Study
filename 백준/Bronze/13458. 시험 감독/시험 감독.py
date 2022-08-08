n = int(input())
peoples = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0
for p in peoples:
    p -= b
    answer += 1
    if p < 0:
        continue
    if p % c == 0:
        answer += (p // c)
    else:
        answer += (p // c + 1)
print(answer)