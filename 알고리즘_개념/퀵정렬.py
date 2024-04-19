# 기준 데이터를 설정하고, 그 기준보다 큰 데이터는 왼쪽에서부터 찾고, 기준보다 작은건 오른쪽에서부터 찾아서 첫번째로 찾은값을 스와프한다.
# 교차가 이루어진경우 피벗과 가장 작은수를 스와프한다.
# 이러한 과정을 반복하면 기준값을 기준으로 왼쪽은 작은값, 오른쪽은 큰값으로 정렬된다. 이렇게 피벗을 기준으로 데이터 묶음을 나누는 작업을 분활divide이라고 한다.
# 가장 많이 사용
# 병합정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
# 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정
# 데이터 분할이 절반씩 일어난다면 onlogn의 시간복잡도를 가진다. 최악의 경우 on^2의 시간복잡도를 가진다.
# 이미 정렬된 데이터에 대해서는 매우 느리게 동작한다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while (left <= right): # 피벗보다 큰 데이터를 찾을 떄까지 반복
            while (left <= end and array[left] <= array[pivot]): # 선형 탐색
                left += 1
            # 피벗보다 작은 데이터를 찾을 때까지 반복
            while (right > start and array[right] >= array[pivot]):
                right -= 1
            if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
                array[right], array[pivot] = array[pivot], array[right] # 엇갈릴때 rifgt이 더 작은 값
            else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
                array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
quick_sort(array, 0, len(array)-1)
print(array)


def quick_sort_python(array, start, end):
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫번째 원소
    except_pivot = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in except_pivot if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in except_pivot if x > pivot] # 분할된 오른쪽 부분
    # 분할 이후 왼쪽, 오른쪽 부분에서 각자 퀵정렬 수행하여 전체 리스트 반환
    return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)