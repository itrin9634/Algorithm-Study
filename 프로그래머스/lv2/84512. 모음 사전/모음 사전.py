def solution(word):
    answer = 0
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(5):
        answer += 1
        fir = alpha[i]
        if word == fir:
            return answer
        for j in range(5):
            answer += 1
            sec = fir + alpha[j]
            if word == sec:
                return answer
            for p in range(5):
                answer += 1
                thr = sec + alpha[p]
                if word == thr:
                    return answer
                for q in range(5):
                    answer += 1
                    four = thr + alpha[q]
                    if word == four:
                        return answer
                    for r in range(5):
                        answer += 1
                        five = four + alpha[r]
                        if word == five:
                            return answer