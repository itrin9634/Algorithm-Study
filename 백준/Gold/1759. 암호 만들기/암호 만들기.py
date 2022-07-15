import sys
input = sys.stdin.readline
l, c = map(int, input().split())
alphas = input().split()
alphas.sort()
vowels = set(['a', 'e', 'i', 'o', 'u'])
cons = set([x for x in alphas if x not in vowels])
tmp = []


def sol(idx):
    if len(tmp) == l and len(set(tmp) & vowels) > 0 and len(set(tmp) & cons) > 1:
        print(''.join(tmp))
        return

    for i in range(idx, c):
        if alphas[i] not in tmp:
            tmp.append(alphas[i])
            sol(i)
            tmp.pop()


sol(0)