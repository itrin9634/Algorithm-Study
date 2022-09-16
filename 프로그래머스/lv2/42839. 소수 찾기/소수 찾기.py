from itertools import permutations
        
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    tmp = []
    for i in range(1, len(numbers)+ 1):
        arr = permutations(numbers, i)
        arr = set(list(arr))

        for j in arr:
            num = int(''.join(j))
            if num not in tmp and is_prime(num):
                tmp.append(num)
    return len(tmp)