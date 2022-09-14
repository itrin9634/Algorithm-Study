def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a, b, k = commands[i]
        answer.append(sorted(array[a-1:b])[k-1])
    return answer