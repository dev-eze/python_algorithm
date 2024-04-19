'''

첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어집니다.
둘째 줄에는 떡의 개별 높이가 주어집니다. 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만 큼 떡을 사갈 수 있습니다.
높이는 10억보다 작거나 같은 양의 정수 또는 0입니다.
적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력합니다.


'''
'''
plan)
적절한 높이를 찾을 때까지 이진 탐색을 수행하여 높이 H를 반복해서 조정.
'현재 이 높이로 자르면 조건을 만족할 수 있는가?'를 확인한 뒤에 조건의 만족 여부('예' 혹은 '아니오)에 따라서 탐색 범위를 좁혀서 해결.
절단기의 높이는 0부터 10억까지의 정수 중 하나여서 선형탐색시 시간초과.
이렇게 큰 탐색 범위를 보면 가장 먼저 이진 탐색을 떠올리자!
'''


'''
시작점 0, 끝점 19, 중간점 19//2 => 9
필요한 떡의 크기 m = 6
-> 가장 긴 떡의 길이 19


'''
array = [19, 15, 10, 17]
start = 0
end = max(array)
m = 6
result = 0

def cut_min(array, start, end, m):
    while (start <= end):
        total_length = 0
        mid = (start + end) // 2

        for x in array:
            if x > mid:
                total_length += x-mid

        if total_length < m:
            end = mid - 1
        else: # 요청한 길이를 만족한경우 최소의 떡을 자르기 위해 시작점 이동
            start = mid + 1
            result = mid

    return result

print(cut_min(array, start, end, m)) # 15

