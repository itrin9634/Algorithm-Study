def solution(N, stages):
    people = len(stages)
    answer = {}
    for i in range(1, N+1):
        if people != 0:
            cnt = stages.count(i)
            answer[i] = cnt / people
            people -= cnt
        else:
            answer[i] = 0
    return sorted(answer, key = lambda x : answer[x], reverse = True)