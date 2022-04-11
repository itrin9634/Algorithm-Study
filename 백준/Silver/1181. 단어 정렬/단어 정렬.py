n = int(input())
words = []
for i in range(n):
    w = input()
    words.append((len(w), w))
words = list(set(words))
words = sorted(words)
for length, word in words:
    print(word)