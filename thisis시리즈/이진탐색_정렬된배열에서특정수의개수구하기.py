'''
n개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
예를들어 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.
단, 이문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받습니다.
없다면 -1 출력합니다.
'''

'''
plan)
시간 복잡도 O(logN)으로 알고리즘을 설계하라는 것은 이진탐색을 이용.
데이터가 정렬되어 있어야 이진 탐색 수행 가능.
특정 값이 등장하는 첫번쨰 위치, 마지막 위치를 찾아 위치 차이를 계산해 문제 해결 가능.
'''

from bisect import bisect_left, bisect_right

def count_by_range(array, search_target):
    array.sort()
    right = bisect_right(array, search_target)
    left = bisect_left(array, search_target)

    result = right - left
    if result == 0:
        return -1
    return result

array = list(map(int, '1122223'))
search_target = 2
# 4

print(count_by_range(array, 2))