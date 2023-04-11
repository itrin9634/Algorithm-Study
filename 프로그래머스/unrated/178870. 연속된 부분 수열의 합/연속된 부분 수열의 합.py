def solution(sequence, k):
    MIN = len(sequence) + 1
    fp, total, cnt  = 0, 0, 0
    answer = []
    
    for sp in range(len(sequence)):
        total += sequence[sp]
        cnt += 1
        if total == k and cnt < MIN:
            MIN = cnt
            answer = [fp, sp]
        while fp <= sp and total > k:
            total -= sequence[fp]
            fp += 1
            cnt -= 1
            if total == k and cnt < MIN:
                MIN = cnt
                answer = [fp, sp]
    return answer