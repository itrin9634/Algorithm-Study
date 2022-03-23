import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1 for i in range(n)]

for i in range(n):
    while stack:
        if a[i] > a[stack[-1]]:
            result[stack.pop()] = a[i]
        else:
            break
    stack.append(i)
print(*result)    