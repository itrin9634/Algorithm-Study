import math

def solution(n, k):
    answer = []
    nums = [i for i in range(1, n+1)]
    while n != 0:
        fact = math.factorial(n-1)
        idx = (k-1) // fact
        answer.append(nums.pop(idx))
        k = k % fact
        n -= 1
    return answer