import sys
from collections import Counter

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
f_arr = Counter(arr)
stack = []
result = [-1] * n

for i in range(n):
    while stack:
        if f_arr[arr[i]] > f_arr[arr[stack[-1]]]:
            result[stack.pop()] = arr[i]
        else:
            break
    stack.append(i)
print(*result)