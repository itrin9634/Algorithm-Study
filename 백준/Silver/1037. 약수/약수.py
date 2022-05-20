num = int(input())
arr = list(map(int, input().split()))
arr.sort()
if num % 2 == 0 : # 짝수일 때
    result = arr[0] * arr[-1]
else:
    result = arr[num//2]
    result = result ** 2
print(result)