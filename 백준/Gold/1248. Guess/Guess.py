def check(idx):
    hap = 0
    for i in range(idx, -1, -1):
        hap += result[i]
        if hap == 0 and signs[i][idx] != 0:
            return False
        elif hap < 0 and signs[i][idx] >= 0:
            return False
        elif hap > 0 and signs[i][idx] <= 0:
            return False
    return True


def solve(idx):
    if idx == n:
        return True
    if signs[idx][idx] == 0:
        result[idx] = 0
        return solve(idx+1)
    for i in range(1, 11):
        result[idx] = signs[idx][idx] * i
        if check(idx) and solve(idx+1):
            return True
    return False


n = int(input())
arr = list(input())
signs = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(i, n):
        temp = arr.pop(0)
        if temp == '+':
            signs[i][j] = 1
        elif temp == '-':
            signs[i][j] = -1
result = [0] * n
solve(0)
print(' '.join(map(str, result)))