from itertools import combinations

# def 로또():
#     while True:
#         # 입력을 받아서 리스트로 변환
#         user_input = list(map(int, input().split()))
#
#         # 첫 번째 숫자 k는 리스트에서 제거
#         k = user_input.pop(0)
#
#         # k가 0이면 종료
#         if k == 0:
#             break
#
#         # 6개의 숫자를 고르는 조합을 출력
#         for each in combinations(user_input, 6):
#             print(' '.join(map(str, each)))
#         # 테스트 케이스 간 빈 줄 출력
#         print()
#
# 로또()


def 로또():
    while True:
        # 입력을 받아서 리스트로 변환
        user_input = list(map(int, input().split()))

        # 첫 번째 숫자 k는 리스트에서 제거
        k = user_input.pop(0)

        # k가 0이면 종료
        if k == 0:
            break

        # 6개의 숫자를 고르는 조합을 출력
        for each in combinations(user_input, 6):
            print(' '.join(map(str, each)))
        # 테스트 케이스 간 빈 줄 출력
        print()


로또()