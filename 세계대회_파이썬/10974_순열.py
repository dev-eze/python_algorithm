def 순열(n, chosen):
    numbers = list(range(1, n+1))
    if len(chosen) == n:
        print(' '.join(map(str, chosen)))
        return

    for i in range(len(numbers)):
        if numbers[i] not in chosen:
            순열(n, chosen + [numbers[i]])


# n = int(input())
# 순열(n, [])

from itertools import permutations

def 순열라이브러리(n, chosen):
    numbers = list(range(1, n+1))

    for each in permutations(numbers, n):
        print(' '.join(map(str, each)))


n = int(input())
순열라이브러리(n, [])