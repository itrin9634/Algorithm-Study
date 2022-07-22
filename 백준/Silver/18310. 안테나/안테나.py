n = int(input())
homes = list(map(int, input().split()))
homes.sort()
print(homes[(n-1)//2])