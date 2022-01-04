n = int(input())

d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

for i in range(n):
    x,y = input().split()
    x = int(x)
    y = int(y)
    d[x-1][y-1]=1

for i in range(1,20):
    for j in range(1,20):
        print(d[i-1][j-1], end=" ")
    print()

