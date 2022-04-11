import heapq

n = int(input())
heap = []
result = []
temp = []
for _ in range(n):
    s = input()
    heapq.heappush(heap, (len(s), s))
length, word = heapq.heappop(heap)
temp.append(word)
while heap:
    t_length, t_word = heapq.heappop(heap)
    if t_length == length:
        if t_word != word:
            temp.append(t_word)
    else:
        temp.sort()
        result += temp
        temp = [t_word]
    length = t_length
    word = t_word
if temp:
    temp.sort()
    result += temp
for i in result:
    print(i)
