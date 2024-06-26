'''
정수 X가 주어졌을 때, 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지입니다.

1. X가 5로 나누어 떨어지면, 5로 나눕니다.

2. X가 3으로 나누어 떨어지면, 3으로 나눕니다.

3. X가 2로 나누어 떨어지면, 2로 나눕니다.

4. X에서 1을 뺍니다.

정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 값을 1로 만들고자 합니다. 연산을 사용하는 횟수의 최

솟값을 출력하세요. 예를 들어,정수가 26이면 다음과 같이 계산해서 3번의 연산이 최솟값입니다.

• 26- 25- 5- 1 # 3번
'''

'''
a=i를 1로 만들기 위한 최소 연산 횟수 점화식은 다음과 같습니다.
ai = min (ai-1, ai/2, ai/3, ai/5) + 1
단, 1을 빼는 연산을 제외하고는 해당 수로 나누어떨어질 때에 한해 점화식을 적용할 수 있습니다.
'''

x = 30000
def getMinCount(x):
    d = [0] * 30001
    d[1] = 1 # 1

    for i in range(2, x+1):
        d[i] = d[i-1] + 1 # 1을 빼는 경우에서의 최소 연산 횟수니까 1을 더함.
        if i % 2 ==0:
            d[i] = min(d[i], d[i//2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)

    return d[x]

print(getMinCount(x))


