import sys
input = sys.stdin.readline
n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0


def check(now):
    for j in range(1, n):
        if abs(now[j] - now[j-1]) > 1:
            return False

        if now[j] < now[j-1]:
            for k in range(l):
                if j + k >= n or used[j + k] or now[j] != now[j + k]:
                    return False

                if now[j] == now[j + k]:
                    used[j + k] = True
        elif now[j] > now[j - 1]:
            for k in range(l):
                if j - k - 1 < 0 or now[j - 1] != now[j- k -1] or used[j-k-1]:
                    return False
                if now[j-1] == now[j-k-1]:
                    used[j-k-1] = True
    return True


#가로 확인
for i in range(n):
    used = [False for _ in range(n)]
    if check(arr[i]):
        cnt += 1

#세로 확인
for i in range(n):
    used = [False for _ in range(n)]
    if check([arr[j][i] for j in range(n)]):
        cnt += 1

print(cnt)