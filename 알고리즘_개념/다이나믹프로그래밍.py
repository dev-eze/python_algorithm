'''
다이나믹 프로그래밍은 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법.
• 의미 계산된 결과(작은 문제)는 나중에 해당 결과가 필요할 때, 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 하는 방법.
• 다이나믹 프로그래밍의 구현은 일반적으로 두 가지 방식(탑다운과 보텀업)으로 구성됨.

한번 계산된 결과를 메모이제이션(Memoization)하고 다시 계산하지 않음.!
완전탐색시 비효율적이어도 다이나믹으로 효율화 할 수 있음.

다이나믹 프로그래밍은 동적 계획법이라고도 부릅니다.
•자료구조에서 동적 할당(Dynamic Allocation)은 '프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법'을 의미하지만
반면에 다이나믹 프로그래밍에서 '다이나믹'은 별다른 의미 없이 사용된 단어라고 함;

다이나믹 프로그래밍은 문제가 다음의 조건을 만족할 때 사용할 수 있습니다.
1. 최적 부분 구조 (Optimal Substructure)
• 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있습니다.
2. 중복되는 부분 문제 (Overlapping Subproblem)
• 동일한 작은 문제를 반복적으로 해결해야 합니다.
'''

'''
피보나치 수열
• 피보나치 수열 다음과 같은 형태의 수열이며, 다이나믹 프로그래밍으로 효과적으로 계산할 수 있습니다.
1,1,2,3,5,8,13,21,34,55,89,
• 점화식이란 인접한 항들 사이의 관계식을 의미합니다.
• 피보나치 수열을 점화식으로 표현하면 다음과 같습니다.
a[n] = a[n-1], + a[n-2]. a[1] = 1, a2 = 1
'''