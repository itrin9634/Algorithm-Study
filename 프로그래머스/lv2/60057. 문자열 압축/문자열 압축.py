def solution(s):
    answer = len(s)
    before = ''
    cur = ''
    cnt = 1
    tmp = ''
    for i in range(1, len(s)+1):
        before = s[:i]
        for j in range(i, len(s) + 1, i):
            cur = s[j:j+i]
            if before == cur:
                cnt += 1
            else:
                if cnt > 1:
                    tmp += str(cnt)
                cnt = 1
                tmp += before
                before = cur
        if cnt > 1:
            tmp += str(cnt)
        tmp += cur
        tmp_length = len(tmp)
        if tmp_length <= answer:
            answer = tmp_length
            sen = tmp
        tmp = ''
    return answer