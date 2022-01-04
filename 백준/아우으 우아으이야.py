num = int(input())
box = []

for i in range(num):
    a = list(map(int,input().split()))
    box.append(a)

for j in range(1,len(box)+1):
    while j < len(box):
        if box[j-1][1] >= box[j][0] :
            if box[j-1][1]<= box[j][1]:
                box[j-1] = [box[j-1][0] , box[j][1] ]
            else:
                box[j-1] = [box[j-1][0] , box[j-1][1] ]
            box.pop(j)
        j = j+1
box2 = []
for x in range(len(box)):
    length = box[x][1]-box[x][0]
    box2.append(length)

print(sum(box2))