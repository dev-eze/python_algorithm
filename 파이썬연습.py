## 문자열 연습1
str = "012345-789"
print(str); ## 012345-789
print(str[7]); ## 7
print(str[1:3]); ## 12
print(str[:3]); ## 012
print(str[4:]); ## 45-789
print(str[-9:]); ## 12345-789
print(str[:-3]); ## 012345-
print(str[-8:]); ## 2345-789
print(str[:-8]); ## 01

## 문자열 연습2
python_text = "python is Amazing"
print(python_text.lower())
print(python_text.upper())
print(python_text[0].isupper())
print(len(python_text))
print(python_text.replace("python", "java"))
index = python_text.index("A")
print(python_text[index].isupper())
print(python_text.find("i"))
print(python_text.find("java")) ## index는 오류 반환, find는 -1반환
index_i = python_text.index("i")
print(index_i)
index_i = python_text.index("i", index_i+1)
print(index_i) ## 14
print(python_text.count("i")) ## 2

## 문자열 연습3
print("베스킨", "라빈스") ## %d 정수
print("베스킨 %d" % 31) ## %d 정수
print("나는 %s를 좋아해요." % "민트초코") ## %s 문자열
print("나는 숫자 %s를 좋아해요." % 7) ## %s 문자열
print("%c로 시작하는 Apple" % "A") ## %c 한글자
print("나는 %s색과 %s색을 좋아해요." %("파란", "노랑"))
print("베스킨 라빈스 {}".format(31))
print("나는 지금 {}과 {}을 주문했다.".format("짬뽕", "짜장면"))
print("나는 지금 {1}과 {0}을 주문했다.".format("짬뽕", "짜장면"))
print("나는 지금 {food1}, {food2}를 주문했다.".format(food1="호두과자", food2="커피"))
str_sound="야옹"
str_date=20240322
print(f"고양이는 {str_sound} 울어요. 오늘은 {str_date}.")