#톱니바퀴들
gears = []
for i in range(4):
    gears.append(list(map(int, list(input()))))


def rotate(num, dir, visited):
    left = gears[num][6]
    right = gears[num][2]
    if dir == 1:  # 시계 방향
        tmp = gears[num][-1]
        for i in range(8):
            next = gears[num][i]
            gears[num][i] = tmp
            tmp = next
    elif dir == -1: # 반 시계 방향
        tmp = gears[num][0]
        for i in range(7, -1, -1):
            next = gears[num][i]
            gears[num][i] = tmp
            tmp = next
    if 0 <= num - 1 < 4 and left != gears[num-1][2] and not visited[num-1]:
        visited[num-1] = True
        rotate(num-1, -dir, visited)
    if 0 <= num + 1 < 4 and right != gears[num + 1][6] and not visited[num + 1]:
        visited[num + 1] = True
        rotate(num + 1, -dir, visited)
    return


# 톱니 바퀴의 점수의 합
def cal_score(one, two, three, four):
    score = 0
    if one:
        score += 1
    if two:
        score += 2
    if three:
        score += 4
    if four:
        score += 8
    return score


k = int(input())  # 회전 횟수
for i in range(k):
    num, dir = map(int, input().split())
    num -= 1
    visited = [False] * 4
    visited[num] = True
    rotate(num, dir, visited)

# 톱니 바퀴의 점수의 합을 출력하기
result = cal_score(gears[0][0], gears[1][0], gears[2][0], gears[3][0])
print(result)
