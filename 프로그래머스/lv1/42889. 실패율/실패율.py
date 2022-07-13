def solution(N, stages):
    arr = []
    for i in range(1, N+1):
        num = 0
        fail = stages.count(i)
        fail_rate = 0
        for s in stages:
            if s >= i:
                num += 1
        if num:
            fail_rate = fail / num
        arr.append((fail_rate, i))
            
    result = sorted(arr, key = lambda x : (-x[0], x[1]))
    answer = []
    for r in result:
        answer.append(r[1])
    return answer