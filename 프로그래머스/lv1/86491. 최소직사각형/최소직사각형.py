def solution(sizes):
    answer = 0
    
    ws = [max(size) for size in sizes]
    hs = [min(size) for size in sizes]
    answer = max(ws) * max(hs)
    
    return answer