def solution(s):
    answer = [0, 0]
    
    while s != '1':
        tmp_0 = s.count('0')
        answer[1] += tmp_0
        answer[0] += 1
        s = bin(len(s) - tmp_0)[2:]
    return answer