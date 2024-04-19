# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘.
# 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능.
# 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행 시간 O(N + K)를 보장.

# 모든 범위를 담을 수 있는 크기의 리스트(배열)을 선언해야 하기 때문에 공간 복잡도가 높다.
# 인덱스별로 몇번씩 등장했는지 구한후 출력하는 방식이다.
# 조건만 만족한다면 빠르다.

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2] # 모든 원소의 값이 0보다 크거나 같다고 가정
def sort(array):
    count = [0] * (max(array) + 1) # 0부터 최대값까지의 리스트 생성 (모든 범위를 담을 수 있는 크기의 리스트, 0으로 초기화)

    for i in range(len(array)):
        count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ') #띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

print(sort(array))



def sort_python(array):
    count = [0] * (max(array) + 1)

    for i in range(len(array)):
        count[array[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]): # 0부터 count리스트의 i인덱스에 담긴 정수만큼(반복 수)
            print(i, end=' ')

print(sort_python(array))
