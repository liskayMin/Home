num = int(input())
box = []
for i in range(num):
    box.append(int(input()))

box.sort()
count = 0
while len(box) != 1:
    count = count + box[0]+box[1]
    box[0] = box[0]+box[1]
    box.pop(1)
    box.sort()

print(count)