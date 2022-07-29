n = int(input())
arr = list(map(int, input().split()))
result = sorted(list(set(arr)))
print(*result)