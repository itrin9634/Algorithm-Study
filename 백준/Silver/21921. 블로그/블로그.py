n, x = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0 #방문자 수
cnt = 0 #기간 수
end = 0
people = 0
days = 0

for start in range(n):
    while days < x and end < n:
        people += arr[end]
        days += 1
        end += 1
    if people == ans:
        cnt += 1
    elif people > ans:
        ans = people
        cnt = 1

    #start뒤로 보내기
    days -= 1
    people -= arr[start]

if ans:
    print(ans)
    print(cnt)
else:
    print('SAD')