python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper) #ture
print(len(python)) # 17
print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index2 = python.index("n",5) # 두번쨰 넣는 곳의 숫자이상 위치에서 찾는듯
# print(index2)

index = python.index("n")
print(index)
index = python.index("n",index+1)
print(index)

# print(python.find("n"))
# print(python.find("Java")) # 없으면 -1을 반환, 그래서 없어도 진행함
# print(python.index("Java")) # 없으면 오류, 그래서 바로 끝남

print(python.count("n")) # n이 몇 번 나왔는지 세줌