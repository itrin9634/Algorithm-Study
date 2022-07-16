from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    
    #원형을 일자로 만들어주기
    for i in range(length):
        weak.append(n + weak[i])
    answer = len(dist) + 1
    
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count-1]
            for index in range(start, start+length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer