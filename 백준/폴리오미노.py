x1 = input()
x2 = list(map(str, x1.split(".")))
print(x2)
x3 = []

for a in x2:
    if len(a) >= 2:
        a = (len(a)//4)*"AAAA" + ((len(a)//2)-(len(a)//4)*2)*"BB" + (len(a)%2)*"X"
        x3.append(a)
    else:
        x3.append(a)
print(x3)

x4 = ""
for i in range(len(x3)):
    x4 = x4 + str(x3[i])

while True:
    for k in range(len(x4)):
        if x4[k] == "X":
            break
        else:
            print(x4)
            break

print(-1)
    