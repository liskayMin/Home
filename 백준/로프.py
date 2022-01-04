n = int(input())
    
list = []
for i in range(n):
    list.append(int(input()))
list.sort()

max_box = []

for a in range(0,len(list)):
    x = list[a]*(len(list)-a)
    max_box.append(x)

print(max(max_box))