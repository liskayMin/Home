num = int(input())
box = list(map(int, input().split()))
box.sort()
box2 = []
box3 = []
for i in range(num):
    a = box[0]
    b = box[len(box)-1]
    box.pop(0)
    box.pop(len(box)-1)
    box2.append([a,b])
    box3.append(a+b)
print(min(box3))