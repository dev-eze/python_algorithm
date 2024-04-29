array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 선택정렬
def 선택정렬():
    pass


# 삽입 정렬
def 삽입정렬(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1): # 인덱스 1부터 1까지 1씩 감소하며 반복하는 문법
            if array [j - 1] > array[j]: # 한 칸씩 왼쪽으로 이동 # 3번째 값 < 2번쨰 값
                array[j], array[j- 1] = array[j- 1], array[j]
            else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
                break
print(삽입정렬(array))

'''
• 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법입니다.
• 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나입니다.
• 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘입니다.
  가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정합니다
'''
def 퀵정렬(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return

    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1
    right = end

    while (left <= right):
    # 피벗보다 큰 데이터를 찾을 때까지 반복
        while (left <= end and array[left] <= array[pivot]):
            left += 1
    # 피벗보다 작은 데이터를 찾을 때까지 반복
        while (right > start and array[right] >= array[pivot]):
            right -= 1
        if (left > right):  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array [right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    퀵정렬(array, start, right - 1)
    퀵정렬(array, right + 1, end)
퀵정렬(array, 0, len(array) - 1)
print(array)



def 파이썬_퀵정렬(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:] #0번째 pivot(start)인덱스를 제외한 모든 값

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return 파이썬_퀵정렬(left) + [pivot] + 파이썬_퀵정렬(right)

print(파이썬_퀵정렬(array))


