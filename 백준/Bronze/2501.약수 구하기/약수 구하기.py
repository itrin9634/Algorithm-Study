n, k = map(int, input().split())
count = 0
result = 0
i = 1

while (i <= n or count == k):
    if((n%i) == 0):
        count +=1
    if(count == k):
        result = i
        break
    i+=1

if(count < k):
    result = 0
print(result)