n, b = map(int, input().split())
d = [0] * 36
result = ""
k = 0
for i in range(36):
    if i >= 10:
        d[i] = chr(ord('A') + k)
        k += 1
    else:
        d[i] = str(i)

while n >= b:
    mod = n % b
    n //= b
    result += d[mod]

if n:
    result += d[n]
print(result[::-1])
