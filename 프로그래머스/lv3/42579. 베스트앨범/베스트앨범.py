def solution(genres, plays):
    answer = []
    hash = dict()
    for i in range(len(genres)):
        if genres[i] in hash:
            hash[genres[i]] += plays[i]
        else:
            hash[genres[i]] = plays[i]
    hash_arr = sorted(list(hash.items()), key = lambda x : -x[1])
    for g, p in hash_arr:
        tmp = []
        for i in range(len(genres)):
            if genres[i] == g:
                tmp.append((plays[i], i))
        
        tmp.sort(key = lambda x: (-x[0], x[1]))
        cnt = 0
        for j in range(len(tmp)):
            cnt += 1
            play, id = tmp[j]
            answer.append(id)
            if cnt == 2:
                break
    return answer