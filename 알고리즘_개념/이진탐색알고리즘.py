'''

이진탐색:
- 정렬되어 있는 리스트에서 탐색범위를 절반씩 좁혀가며 데이터를 탐색하는 방법.
- 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다. (인덱스)

이진탐색의 시간복잡도:
단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 log2 N에 비례합니다.
• 예를 들어 초기 데이터 개수가 32개일 때, 이상적으로 1단계를 거치면 16개가량의 데이터만 남습니다
• 2단계를 거치면 8개가량의 데이터만 남습니다.
• 3단계를 거치면 4개가량의 데이터만 남습니다.
• 다시 말해 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 0(log N)을 보장합니다.

순차탐색:
- 리스트안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법.

'''

'''
예) 시작점 0, 끝점 9, 중간점은 (9/2) => rount(4.5) => 4
index4의 값이 찾는 값보다 크다면 그 이후 오른쪽은 보지않고 끝점을 4, 즉 중간점에서 한칸 왼쪽으로 옮겨 3으로 이동, 또 중간점을 찾아 탐색.
0~3 -> 1.5 -> 1
중간점 같이 탐색값보다 작다면 왼쪽은 보지않고 시작점을 중간점, 1에서 한칸 오른쪽으로 옮겨 2로 이동, 또 중간점을 찾아 탐색.

'''

# 이진탐색 소스코드 구현(재귀함수)
def binary_search(array, search_target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == search_target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    if array[mid] > search_target:
        return binary_search(array, search_target, start, mid-1)
    if array[mid] < search_target:
        return binary_search(array, search_target, mid+1, end)

print(binary_search([1,3,5,7,9,11,13,15,17,19], 7, 0, 9)) # end = n - 1



'''
bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
bisect_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
'''

'''
문제) 값이 특정 범위에 속하는 데이터 개수 구하기
값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
'''
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8] # 1, 2,^ 4, 4,^ 8
x = 4
print(bisect_left(a, x)) # 2
print(bisect_right(a, x)) # 4

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index # right_index - left_index = 두수 사이의 개수


# 배열 선언
a= [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
# 값이 4인 데이터 개수 출력 -> left, right 같게 입력
print(count_by_range(a, 4, 4)) # 2
# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3)) # 6

# 파라메트릭 서치
'''
- 파라메트릭 서치란 최적화 문제를 결정 문제(예 혹은 아니오)로 바꾸어 해결하는 기법
- 일반적으로 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결 가능
- 예시) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제 

- 최적화문제란 어떤 함수의 값을 낮추거나 높이는 문제
- 결정 문제(예 혹은 아니오)
'''
