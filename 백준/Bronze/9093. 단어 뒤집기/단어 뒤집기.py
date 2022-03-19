n = int(input())

for i in range(n):
    result = []
    data = input().split()
    for j in range(len(data)):
        word = data[j]
        result.append(word[::-1])
    result1 = " ".join(result)
    print(result1)
        
        
        
        