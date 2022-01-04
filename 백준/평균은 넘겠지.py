import sys
input = sys.stdin.readline

num = int(input())
lst = []
for i in range(num):
    lst.append(list(map(int,input().split())))

for i in range(len(lst)):
    lst[i][0] = (sum(lst[i])-lst[i][0])/(len(lst[i])-1)

for i in range(len(lst)):
    x = 0
    for j in range(len(lst[i])):
        if lst[i][j] > lst[i][0]:
            x = x + 1
    lst[i][0] = x/(len(lst[i])-1)*100

for i in range(len(lst)):
    print("{0:.3f}%".format(lst[i][0]))
