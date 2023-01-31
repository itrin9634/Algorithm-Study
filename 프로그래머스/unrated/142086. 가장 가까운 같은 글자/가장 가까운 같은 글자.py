from collections import defaultdict

def solution(s):
    idx_dict = defaultdict(int) #가장 나중에 나온 문자가 몇 번째 인덱스에 나왔는지 담는 dict
    answer = []
    
    for i in range(len(s)):
        if idx_dict[s[i]] == 0: #이전에 나오지 않은 수일 때
            answer.append(-1)
        else:
            answer.append(i + 1 - idx_dict[s[i]])
        idx_dict[s[i]] = i + 1
    return answer