level = int(input())
box = []
for i in range(level):
    box.append(int(input()))

box.reverse()
reduction = 0
for a in range(1,len(box)):
    if box[a] >= box[a-1]:
        reduction = reduction + (box[a]-box[a-1]+1)
        box[a] = box[a] - (box[a]-box[a-1]+1)


print(reduction)