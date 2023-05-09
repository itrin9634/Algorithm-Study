def solution(record):
    answer = []
    nic_dic = {}
    msg_dic = {'Enter': '님이 들어왔습니다.', 'Leave' : '님이 나갔습니다.'}
    for r in record:
        tmp = list(r.split())
        if len(tmp) == 3:
            nic_dic[tmp[1]] = tmp[2]
    
    for r in record:
        tmp = list(r.split())
        if tmp[0] == 'Change':
            continue
        answer.append(nic_dic[tmp[1]] + msg_dic[tmp[0]])
    
    return answer