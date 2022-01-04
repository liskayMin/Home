# 딕셔너리 dictionary
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
# print(cabinet[5]) 에러나오고 멈춤

print(cabinet.get(3))
print(cabinet.get(100))
# print(cabinet.get(5)) / 없으면 None 출력 후 계속 나감
print(cabinet.get(5))

print(cabinet.get(5,"사용가능")) # None 대신 "사용가능"이 나오게 했음
print("hi")

# 안에 있는지 확인
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님(업데이트, 추가)
print(cabinet)
cabinet["A-3"] = "김종국"
print(cabinet)
cabinet["C-20"] = "조세호"

# 간 손님
del cabinet["A-3"]
print(cabinet)
 
# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)