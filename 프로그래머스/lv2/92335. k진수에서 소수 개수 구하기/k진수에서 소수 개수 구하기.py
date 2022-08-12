def isPrime(s):
    n = int(s)
    for i in range(2, int(n** 0.5) + 1):
        if int(n) % i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    arr = []
    while n > 0:
        arr.append(n % k)
        n //= k
    s = ''.join(map(str, (arr[::-1])))
    nums = s.split('0')
    print(nums)
    for n in nums:
        if len(n) <= 0 or int(n) <= 1:
            continue
        if isPrime(n):
            answer += 1
    return answer