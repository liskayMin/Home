# 애완동물을 소개해 주세요~
animal = "고양이"
name = "해피"
age = 2
hobby = "낮잠"
is_adult = age>=3


print("우리집 " + animal + "의 이름은 "+ name + "예요")
print(name + "는 " + str(age)+"살이며, " + hobby + "을 아주 좋아해요")
# ,로 연결하면  str 함수를 안써도 되지만, 띄어쓰기가 생긴다.
print(name,"는 ",age,"살이며, ",hobby,"을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

# 주석은  샾 #
# 주석 여러개 설정 및 해지 :   ctrl + /  #
''' 여러문장은 작은따옴표 3개'''