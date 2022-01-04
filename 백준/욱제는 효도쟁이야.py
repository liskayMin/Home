city = int(input())
box = list(map(int, input().split()))

print(sum(box)-max(box))