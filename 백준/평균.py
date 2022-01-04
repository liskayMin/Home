num = int(input())
lst = list(map(int, input().split()))
a = max(lst)
for i in range(len(lst)):
    lst[i] = lst[i]/a


print(sum(lst)/len(lst)*100)