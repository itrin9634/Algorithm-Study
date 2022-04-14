def isCall(phones, n):
    phones.sort()
    for i in range(n-1):
        if phones[i] == phones[i+1][:len(phones[i])]:
            print('NO')
            return
    print('YES')
    return


t = int(input())
for i in range(t):
    phone = []
    n = int(input())
    for j in range(n):
        phone.append(input())
    isCall(phone, n)