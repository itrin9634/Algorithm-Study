def gcd(x,y):
    while y:
        x, y = y, x%y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

def solution(arr):
    while len(arr) >= 2:
        fir = arr.pop()
        sec = arr.pop()
        arr.append(lcm(fir, sec))
    answer = arr[0]
    return answer