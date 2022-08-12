import math

def solution(begin, end):
    answer = []
    
    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
        else:
            sqrt = int(math.sqrt(i))
            for j in range(2, sqrt + 1):
                mok = i // j
                if mok > 10 ** 7:
                    continue
                if i % j == 0:
                    answer.append(mok)
                    break
            else:
                answer.append(1)
                    
    return answer