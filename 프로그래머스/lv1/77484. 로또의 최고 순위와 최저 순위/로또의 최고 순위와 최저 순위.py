def cal_rank(cnt):
    a = [6, 5, 4, 3, 2]
    rank = 0
    if cnt in a:
        rank = a.index(cnt) + 1
    else:
        rank = 6
    return rank

def solution(lottos, win_nums):
    result = []
    cnt = lottos.count(0)
    answer = 0
    for l in lottos:
        if l in win_nums:
            answer += 1
    result.append(cal_rank(answer + cnt))
    result.append(cal_rank(answer))
    return result