n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
tmp = 0 #부분 수열의 갯수
count = 0 # 지우려는 홀수 갯수
end = 0 # 끝 포인터
for start in range(n):
    while (count <= k and end < n):
        if arr[end] % 2 == 1: #홀수:
            count += 1
        else:
            tmp += 1
        end += 1
    result = max(result, tmp)
    #start 뒤로 보내기
    if arr[start] % 2 == 1: #홀수
        count -= 1
    else:
        tmp -= 1

print(result)