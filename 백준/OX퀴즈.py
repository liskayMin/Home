num = int(input())
lst = []
for i in range(num):
    lst.append(list(map(str,input())))

for i in range(len(lst)) :
    count = 0
    for j in range(len(lst[i])):
        while lst[i][j] == "O":
            count = count + 1
            if j ==0:
                break
            j = j-1
    lst[i].insert(0,count)
    print(count)
