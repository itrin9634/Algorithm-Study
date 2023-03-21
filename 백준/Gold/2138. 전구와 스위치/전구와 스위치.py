n = int(input())
state = list(map(int, input()))
goal = list(map(int, input()))

def zeroClick(state):
    cnt = 1
    state[0] = 1 - state[0]
    state[1] = 1 - state[1]

    for i in range(1, n):
        if state[i-1] != goal[i-1]:
            cnt += 1
            state[i-1] = 1- state[i-1]
            state[i] = 1 - state[i]
            if i != (n - 1):
                state[i+1] = 1 - state[i+1]
    if state == goal:
        return cnt
    else:
        return -1

def zeroNoClick(state):
    cnt = 0
    for i in range(1, n):
        if state[i-1] != goal[i-1]:
            cnt += 1
            state[i-1] = 1- state[i-1]
            state[i] = 1 - state[i]
            if i != (n - 1):
                state[i+1] = 1 - state[i+1]
    if state == goal:
        return cnt
    else:
        return -1

res1 = zeroClick(state[:])
res2 = zeroNoClick(state[:])
if res1 >= 0 and res2 >= 0:
    print(min(res1, res2))
elif res1 >= 0 and res2 < 0:
    print(res1)
elif res1 < 0 and res2 >= 0:
    print(res2)
else:
    print(-1)