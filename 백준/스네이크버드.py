N, L = input().split()
N = int(N)
L = int(L)

count = 0
box = []
box = list(map(int, input().split()))
box.sort()

for j in box:
    if L>=j:
        L=L+1
        count = 1

print(L)