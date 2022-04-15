n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
INF = int(1e9)
board = [[INF] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            board[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])
for i in range(n):
    for j in range(n):
        if board[i][j] != INF:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
