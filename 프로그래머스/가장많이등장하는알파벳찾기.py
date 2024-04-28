'''
문제 설명
이 문제에는 표준 입력으로 문자열, mystr이 주어집니다. mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성해주세요.

제한 조건
mystr의 원소는 알파벳 소문자로만 주어집니다.
mystr의 길이는 1 이상 100 이하입니다.

예시
input	output
'aab'	'a'
'dfdefdgf'	'df'
'bbaa'	'ab'
'''

from collections import Counter

# my_str = input().strip()
my_str1 = list('aab')
my_str2 = list('dfdefdgf')
my_str3 = list('bbaa')
def solution(my_str):
    counter = Counter(my_str)
    #max_freq = max(counter.values())
    #max_freq2 = counter.most_common()[0][1]
    result = [key for key, freq in sorted(counter.most_common(), key=lambda x: x[1], reverse=True) if freq == counter.most_common(1)[0][1]]
    result.sort()
    #return ''.join(result)
    return ''.join(sorted(result))

print(solution(my_str1))
print(solution(my_str2))
print(solution(my_str3))

