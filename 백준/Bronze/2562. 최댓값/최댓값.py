MAX = -int(1e9)
result = 0
for i in range(1, 10):
    n = int(input())
    if n > MAX:
        MAX = n
        result = i
print(MAX)
print(result)
