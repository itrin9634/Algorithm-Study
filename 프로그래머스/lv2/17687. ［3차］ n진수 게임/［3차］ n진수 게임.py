arr = [0]

# n진수 수 구하는 함수
def cal(n, x):
    global arr
    tmp = []
    while x:
        mod = x % n
        if mod >= 10:
            mod = chr((mod - 10) + ord('A'))
        tmp.append(mod)
        x //= n
    arr += tmp[::-1]
        

def solution(n, t, m, p):
    answer = ''
    p -= 1
    x = 0
    length = len(arr)
    while t > 0:
        if p < length:
            answer += str(arr[p])
            t -= 1
            p += m
        else:
            x += 1
            cal(n, x)
            length = len(arr)
        
    return answer