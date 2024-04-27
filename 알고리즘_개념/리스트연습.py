## 리스트 연습

names = ["유재석", "조세호", "하하"]
print(names)
print(names[0])
print(names.index("유재석"))

names.append("박명수")
print(names)
names.insert(1, "새로운 멤버")
print(names)
print(names.pop()) ## 맨뒤에서 하나씩 꺼냄
print(names)

print(names.pop()) ## 맨뒤에서 하나씩 꺼냄
print(names)
names.append("유재석")
print(names.count("유재석"))
names.remove("유재석")
print(names.count("유재석"))

num_list=[1,2,3,4,5,6,7,8,9]
num_list.reverse()
print(num_list)
num_list.sort()
print(num_list)
## num_list.clear() ## []

## 다양한 자료형과 함께 사용 가능
mix_list=["가", "나", 1, "다", 3]
print(mix_list)
num_list.extend(mix_list) ## 리스트 확장
print(num_list)

## 사전 (key : value), key 중복 x
cabinet = {3:"유재석", 100:"하하"}
print(cabinet[3])
print(cabinet[100])
