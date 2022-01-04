a = int(input())
box = []
quarter = 0
dime = 0
nickel = 0
penny = 0

for i in range(a):
    box.append(int(input()))
for j in box:
    if 25 <= j:
        quarter = j//25
        j = j%25
    if 10 <= j:
        dime = j//10
        j = j%10
    if 5 <= j:
        nickel = j//5
        j = j%5
    if 1 <= j:
        penny = j//1
        j = j%1
    print(quarter, dime, nickel, penny)
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0