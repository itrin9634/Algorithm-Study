def dfs(queen, row, n):
    count = 0
    if row == n:
        return 1
    for col in range(n):
        queen[row] = col
        
        for x in range(row):
            # 가로로 겹치는지 확인
            if queen[x] == queen[row]:
                break
            #대각선으로 겹치는지 확인
            if abs(queen[row] - queen[x]) == (row-x):
                break
        else:
            count += dfs(queen, row+1, n)
    return count


def solution(n):
    return dfs([0]*n, 0, n)