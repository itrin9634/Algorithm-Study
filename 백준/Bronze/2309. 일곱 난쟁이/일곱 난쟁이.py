from itertools import combinations
arr = []
result = []
for i in range(9):
    n = int(input())
    arr.append(n)
comb = list(combinations(arr, 7))
for c in comb:
    if sum(c) == 100:
        for i in c:
            result.append(i)
        break

result.sort()
for i in result:
    print(i)