def solution(n, lost, reserve):
    n_lost = list(set(lost) - set(reserve))
    n_reserve = list(set(reserve) - set(lost))
    
    for i in range(len(n_reserve)):
        if n_reserve[i] - 1 in n_lost:
            n_lost.remove(n_reserve[i]-1)
            continue
        elif n_reserve[i] + 1 in n_lost:
            n_lost.remove(n_reserve[i] + 1)
    
    return n - len(n_lost)