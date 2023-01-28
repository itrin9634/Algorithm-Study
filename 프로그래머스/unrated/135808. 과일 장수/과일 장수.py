def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    length = len(score)
    cnt = length // m  # 나오는 상자 갯수
    idx = m - 1
    for i in range(1, cnt + 1):
        answer += (score[idx] * m)
        idx += m
    
    return answer