def solution(id_list, report, k):
    answer = []
    dic = {}
    for i in range(len(id_list)):
        dic[id_list[i]] = int(i)
    reversed_dic= dict(map(reversed, dic.items()))
    reports = [[] * len(id_list) for _ in range(len(id_list))]
    counts = [0] * len(id_list)
    
    # 각 사람마다 신고한 사람 저장
    for i in range(len(report)):
        a, b = report[i].split()
        if b in reports[dic[a]]:
            continue
        reports[dic[a]].append(b)
        counts[dic[b]] += 1
    
    # 정지된 사람 목록
    stop_users = []
    for i in range(len(counts)):
        if counts[i] >= k:
            stop_users.append(reversed_dic[i])
    
    for i in range(len(reports)):
        cnt = 0
        for j in range(len(stop_users)):
            if stop_users[j] in reports[i]:
                cnt += 1
        answer.append(cnt)
    return answer