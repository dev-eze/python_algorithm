def 순열함수(arr, chosen, r):
    if len(chosen) == r:
        print(chosen)
        return

    for i in range(len(arr)):
        if arr[i] not in chosen:  # 이미 선택된 원소는 중복해서 선택하지 않음
            순열함수(arr, chosen + [arr[i]], r)

# 예시
arr = ['A', 'B', 'C']
순열함수(arr, [], 2)



from itertools import permutations

# 입력 받기
N = int(input())

# 1부터 N까지의 수로 이루어진 리스트 생성
numbers = list(range(1, N + 1))

# 순열 생성 및 출력
for perm in permutations(numbers):
    print(' '.join(map(str, perm)))