import sys

N, K = map(int, sys.stdin.readline().strip().split())
table = str(sys.stdin.readline().strip())
lst = []
lst2 = []
for i in table:
    lst.append(i)
    lst2.append("0")
    
for i in range(len(lst)):
    lst2[i] = lst[len(lst)-i-1]

count = 0
count2 = 0

for i in range(len(lst)):
    if lst[i] == 'P':
        if i == 0:
            for j in range(i+1,i+K+1):
                if lst[j] =='H':
                    lst[j] = 'C'
                    count = count +1
                    break
        elif  i == 1:
            for j in range(i-1,i+K+1):
                if lst[j] =='H':
                    lst[j] = 'C'
                    count = count +1
                    break
        elif i == N-1:
            for j in range(i-K-1,i):
                if lst[j] =='H':
                    lst[j] = 'C'
                    count = count +1
                    break
        elif i == N-2:
            for j in range(i-K-2,i+1):
                if lst[j] =='H':
                    lst[j] = 'C'
                    count = count +1
                    break
        else:
            for j in range(i-K,i+K+1):
                if lst[j] =='H':
                    lst[j] = 'C'
                    count = count +1
                    break
    else:
        continue

for i in range(len(lst2)):
    if lst2[i] == 'P':
        if i == 0:
            for j in range(i+1,i+K+1):
                if lst2[j] =='H':
                    lst2[j] = 'C'
                    count2 = count2 +1
                    break
        elif  i == 1:
            for j in range(i-1,i+K+1):
                if lst2[j] =='H':
                    lst2[j] = 'C'
                    count2 = count2 +1
                    break
        elif i == N-1:
            for j in range(i-K,i+1):
                if lst2[j] =='H':
                    lst2[j] = 'C'
                    count2 = count2 +1
                    break
        elif i == N-2:
            for j in range(i-K-1,i+2):
                if lst2[j] =='H':
                    lst2[j] = 'C'
                    count2 = count2 +1
                    break
        else:
            for j in range(i-K,i+K+1):
                if lst2[j] =='P':
                    lst2[j] = 'C'
                    count2 = count2 +1
                    break
    else:
        continue

print(min(count, count2))