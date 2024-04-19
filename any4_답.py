n = int(input())

eat = list(map(int, input().split()))
hot = list(map(int, input().split()))

for i in range(n):
    dic = dict()
    dict.put(i, [eat[i], hot[i]])

# dic을 데우는 시간으로 내림차순 정렬
dic = sorted(dic.items(), key=lambda x: x[1][0], reverse=True)

for i in range(n):
    get = dic.get(i)
    if get[1] > get[0]:
		result += get[1]



