N = int(input())
prime_list = [True] * 1000001

for i in range(2, 1001):
    if prime_list[i]:
        for j in range(i+i, len(prime_list), i):
            prime_list[j] = False


def count_primes(n):
    result = 0
    for x in range(2, n // 2 + 1):
        if prime_list[x] and prime_list[n - x]:
            result += 1
    return result


for j in range(N):
    print(count_primes(int(input())))