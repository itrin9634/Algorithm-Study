def solution(files):
    answer = []
    dic = dict()
    temp = []
    for i in range(len(files)):
        dic[i] = files[i]
        tmp = files[i].upper()
        head, num, tail = '', '', ''
        for j in range(len(tmp)):
            if not num and not tmp[j].isdigit():
                head += tmp[j]
            elif num and not tmp[j].isdigit():
                tail += tmp[j]
            elif tail:
                tail += tmp[j]
            elif tmp[j].isdigit():
                num += tmp[j]
        temp.append((head, int(num), i))
    temp.sort(key = lambda x : (x[0], x[1], x[2]))
    for h, n, i in temp:
        answer.append(dic[i])
    return answer