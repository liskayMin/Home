total = int(input())
a = input().split()

for i in range(len(a)):
    a[i] = int(a[i])

answer = 10000000000000

for x in a:
    for j in a:
        if x>j:
            break
        else:
            if x<answer:
                answer = x

print(answer)