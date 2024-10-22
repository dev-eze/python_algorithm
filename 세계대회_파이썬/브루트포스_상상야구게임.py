n = int(input())
questions = []

from itertools import permutations

for i in range(n):
    number, strike, ball = map(int, input().split())
    questions.append(((list(map(int, str(number)))), strike, ball))

# np3
candidates = list(permutations(range(1, 10), 3))
answer = 0

for guess in candidates:
    is_answer = True
    for number, strike, ball in questions:
        real_strike = 0
        real_ball = 0

        for i in range(3):
            # 비교
            if guess[i] == number[i]:
                real_strike += 1
            elif guess[i] in number:
                real_ball += 1

        if real_strike != strike or real_ball != ball:
            is_answer = False
            break
    if is_answer:
        answer += 1

print(answer)