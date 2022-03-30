a, b = map(int, input().split())
n = int(input())
array = list(map(int, input().split()))
num_10 = 0
array.reverse()

for i in range(len(array)):
    num_10 += array[i] * (a ** i)

result = []

while num_10 != 0:
    result.append(num_10 % b)
    num_10 //= b

result.reverse()
print(*result)