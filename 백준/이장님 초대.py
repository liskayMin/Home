n = int(input())
box = []
box = list(map(int, input().split()))
box.sort(reverse = True)
box2 = []

for i in range(len(box)):
    x  = i + 2 + box[i]
    box2.append(x)

print(box2)