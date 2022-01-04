lst = []
for i in range(9):
    lst.append(int(input()))

for i in range(len(lst)):
    if lst[i] == max(lst) :
        print(max(lst))
        print(i+1)