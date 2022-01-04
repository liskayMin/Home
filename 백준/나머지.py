lst = []
for i in range(10):
    lst.append(int(input()))

for i in range(len(lst)):
    lst[i] = lst[i]%42

lst = list(set(lst))
print(len(lst))