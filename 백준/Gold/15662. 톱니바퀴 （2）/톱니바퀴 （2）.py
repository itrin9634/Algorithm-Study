from collections import deque

# 톱니 바퀴의 개수 및 입력 받기
gears = []
t = int(input())
for i in range(t):
    gears.append(list(map(int, list(input()))))


def check(start, dir, visited):
    rotated_list = []
    q = deque()
    q.append((start, dir))
    visited[start] = True
    rotated_list.append((start, dir))

    while q:
        now, d = q.popleft()

        # 왼쪽 확인
        if 0 <= now - 1 < t and not visited[now-1] and gears[now-1][2] != gears[now][6]:
            visited[now-1] = True
            q.append((now-1, -d))
            rotated_list.append((now-1, -d))

        # 오른쪽 확인
        if 0 <= now + 1 < t and not visited[now+1] and gears[now+1][6] != gears[now][2]:
            visited[now+1] = True
            q.append((now+1, -d))
            rotated_list.append((now+1, -d))
    return rotated_list


def rotate(num, dir):
    if dir == 1:
        tmp = gears[num][-1]
        for i in range(8):
            next = gears[num][i]
            gears[num][i] = tmp
            tmp = next

    elif dir == -1:
        tmp = gears[num][0]
        for i in range(7, -1, -1):
            next = gears[num][i]
            gears[num][i] = tmp
            tmp = next
    return


k = int(input())  #회전 횟수
for i in range(k):
    num, dir = map(int, input().split())
    num -= 1
    visited = [False] * t
    rotate_list = check(num, dir, visited)
    for n, d in rotate_list:
        rotate(n, d)

ans = 0
for i in range(len(gears)):
    if gears[i][0]:
        ans += 1

print(ans)