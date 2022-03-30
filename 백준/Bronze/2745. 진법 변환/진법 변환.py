n, b = input().split()
t = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = n[::-1]
k = 0
result = 0
for i in range(len(n)):
    result += t.index(str(n[i])) * (int(b) ** k)
    k += 1
print(result)