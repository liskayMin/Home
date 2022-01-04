lst = []
lst.append(list(map(int,input())))

while len(lst) == 1 :
    while len(lst[0]) == 1:
        lst[0].insert(0,0)
        print(lst)
    if lst[0][0] + lst[0][1] >= 10:
        lst.insert(0,[lst[0][1], lst[0][0]+lst[0][1]-10])
        print(lst)
    elif lst[0][0] + lst[0][1] < 10:
        lst.insert(0,[lst[0][1], lst[0][0]+lst[0][1]])
        print(lst)
    else:
        print("오류1")
while (lst[0][0] != lst[len(lst)-1][0]) or (lst[0][1] != lst[len(lst)-1][1]):
    while len(lst[0]) == 1:
        lst[0].insert(0,0)
        print(lst)
    if lst[0][0] + lst[0][1] >= 10:
        lst.insert(0,[lst[0][1], lst[0][0]+lst[0][1]-10])
        print(lst)
    elif lst[0][0] + lst[0][1] < 10:
        lst.insert(0,[lst[0][1], lst[0][0]+lst[0][1]])
        print(lst)
    else:
        print("오류1")

print(len(lst)-1)
