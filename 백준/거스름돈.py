a = int(input())
b = 1000-a

list = [500,100,50,10,5,1]
coin = 0

for i in list:
    if i<=b:
        coin += b//i
        b = b%i

print(coin)