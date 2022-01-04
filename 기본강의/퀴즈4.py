# from random import *
# list = [1,2,3,4,5]
# print(list)
# shuffle(list)
# print(list)
# print(sample(list,1))
'''  내꺼
list = []
for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
    list.append(i)

print(list)

from random import *

shuffle(list)
print(list, type(list))
chicken = list[0]
print(chicken,type(chicken))
list.pop(0)

coffee = []

for i in [1,2,3] :
    shuffle(list)
    coffee.append(list[0])
    list.pop(0)

print(chicken)
print(coffee)
'''    

from random import *
users = range(1,21) # 1부터 21 직전까지
# print(users, type(users))
users = list(users)
# print(users, type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users,4) # 4명 중에서 1명은 치킨, 3명은 커피 주면 됨
print( " -- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print( " -- 축하합니다. --")
