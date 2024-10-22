def 조합함수(arr, start, chosen, r):
    if len(chosen) == r:
        print(chosen)
        return

    for i in range(start, len(arr)):
        조합함수(arr, i+1, chosen + [arr[i]], r)

# 예시
arr = ['A', 'B', 'C']
조합함수(arr, 0, [], 2)
