a, b = input().split()
a = int(a)
b = int(b)

list = []

for i in range(a):
    list.append(int(input()))

list.sort(reverse=True)
coin = 0

for i in list:
    if i<=b:
        coin += b//i
        b = b%i

print(coin)