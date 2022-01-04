a = int(input())
b = int(input())
c = int(input())
mul = str(a*b*c)
lst = list(map(int, mul))

for i in range(10):
    count = 0
    for j in lst:
        if i == j:
            count += 1
    print(count)