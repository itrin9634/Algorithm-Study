n = int(input())
signs = input().split()
visited = [False] * 10
cur_nums = []
mn, mx = "", ""


#부등호 맞는지 확인
def is_correct_sign(x, y, sign):
    flag = False
    if sign == '<':
        if x < y:
            flag = True
    elif sign == '>':
        if x > y:
            flag = True
    return flag


def dfs(curr, cnt):
    global mn
    global mx

    if cnt == (n+1):
        if len(mn) == 0:
            mn = (''.join(map(str, cur_nums)).rjust(n+1, '0'))
        else:
            mx = (''.join(map(str, cur_nums)).rjust(n+1, '0'))
        return

    for i in range(10):
        if not visited[i] and is_correct_sign(curr, i, signs[cnt-1]):
            cur_nums.append(i)
            visited[i] = True
            dfs(i, cnt + 1)
            cur_nums.remove(i)
            visited[i] = False


for i in range(10):
    if not visited[i]:
        visited[i] = True
        cur_nums.append(i)
        dfs(i, 1)
        cur_nums.remove(i)
        visited[i] = False

print(mx)
print(mn)