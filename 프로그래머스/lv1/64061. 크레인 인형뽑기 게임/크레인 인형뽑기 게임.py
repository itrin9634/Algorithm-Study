def solution(board, moves):
    answer = 0
    basket = []
    before = 0 # 이전 인형의 모양
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                doll = board[i][m-1]
                board[i][m-1] = 0
                if doll == before:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(doll)
                if basket:
                    before = basket[-1]
                break
    return answer