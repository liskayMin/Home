num = int(input())

box = []
for i in range(num):
    box.append(list(map(int, input().split())))

box.sort(key = lambda x:x[1])
print(box)

