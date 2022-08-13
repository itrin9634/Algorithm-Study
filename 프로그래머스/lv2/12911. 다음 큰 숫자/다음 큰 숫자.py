def solution(n):
    binary = bin(n)[2:]
    cnt = binary.count('1')
    for i in range(n+1, 1000001):
        temp = bin(i)[2:]
        if temp.count('1') == cnt:
            return i