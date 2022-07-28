from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
pers = list(permutations(arr, n))
result = 0
for p in pers:
    tmp = 0
    for i in range(1, len(p)):
        tmp += abs(p[i]-p[i-1])
    result = max(result, tmp)
print(result)