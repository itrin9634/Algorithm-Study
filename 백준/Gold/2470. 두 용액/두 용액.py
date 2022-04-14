n = int(input())
arr = list(map(int, input().split()))
arr.sort() # 오름차순 정렬
start = 0
end = n - 1
mix = abs(arr[start] + arr[end])
s = 0
e = n - 1
while start < end:
    if abs(arr[start] + arr[end]) < mix:
        mix = abs(arr[start] + arr[end])
        s = start
        e = end
    if arr[start] + arr[end] < 0:
        start += 1
    else:
        end -= 1
print(arr[s], arr[e])