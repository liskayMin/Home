import sys
input = sys.stdin.readline

lst1 = []
lst2 = []
N = int(input())
A, B  = input().split()
A = int(A)
B = int(B)
cal_dough = int(input())
lst1.append([A, cal_dough])


for i in range(N):
    lst2.append([B, int(input())])
lst2.sort(reverse = True)
lst1.extend(lst2)

for j in range(len(lst1)):
    if j == 0:
        continue
    else:
        lst1[j][0] = lst1[j][0] + lst1[j-1][0]
        lst1[j][1] = lst1[j][1] + lst1[j-1][1]

lst3 = []
for i in range(len(lst1)):
    lst3.append(int(lst1[i][1]/lst1[i][0]))

print(max(lst3))