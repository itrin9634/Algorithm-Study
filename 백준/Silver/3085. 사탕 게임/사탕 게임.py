def check(arr):
    n = len(arr)
    answer = 1
    # 행
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
                answer = max(cnt, answer)
            else:
                cnt = 1

        # 열
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
                answer = max(cnt, answer)
            else:
                cnt = 1
    return answer


n = int(input())
arr = [list(input()) for _ in range(n)]
maxNum = 0

for i in range(n):
    for j in range(n-1):
        if arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            maxNum = max(check(arr), maxNum)
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        if arr[j][i] != arr[j+1][i]:
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
            maxNum = max(check(arr), maxNum)
            arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
print(maxNum)