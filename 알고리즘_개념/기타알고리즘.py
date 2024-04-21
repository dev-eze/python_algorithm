# 소수 구하기
# 시간복잡도 O(N) (1~N까지의 수 중 소수 찾기)
'''
x + 1까지 반복하면 불필요한 연산이 추가됩니다. 왜냐하면 어떤 수 x를 x로 나누면 항상 나머지가 0이기 때문입니다.
따라서 x가 소수인지 아닌지를 판별하는 데는 x를 x로 나누는 연산은 필요하지 않습니다.
그래서 for i in range(2, x):를 사용하여 2부터 x - 1까지의 수로 x를 나누어 보는 것입니다.
'''
def is_prime_number(x):
    for i in range(2, x):
        print(i)
        if x % i == 0:
            return False
    return True

print(is_prime_number(4)) # 4는 소수가 아님
print(is_prime_number(7))
print(is_prime_number(11))
print(is_prime_number(9))

'''
약수의 성질
• 예를 들어 16이 2로 나누어떨어진다는 것은 8로도 나누어떨어진다는 것을 의미합니다.

• 모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이루는 것을 알 수 있습니다.

• 예를 들어 16의 약수는 1, 2, 4, 8, 16입니다.

• 이때 2X8= 16은 8X 2 = 16과 대칭입니다.

• 따라서 우리는 특정한 자연수의 모든 약수를 찾을 때 가운데 약수(제곱근)까지만 확인하면 됩니다.  

-> 중간값의 제곱근까지만
'''
# 개선된 소수 구하기
# 시간복잡도 O(N 1/2) (1~N 절반까지의 수 중 소수 찾기)
import math
def is_prime_number_sqrt(x): #  2부터 x의 제곱근까지의 모든 수를 확인하며 x가 해당 수로 나누어떨어지면 소수가 아님
    #for i in range(2, int(math.sqrt(x))+1): # +1을 해주어 제곱근정수까지 계산에 포함되도록 한다.
    for i in range(2, int(x^2)+1): # +1을 해주어 제곱근정수까지 계산에 포함되도록 한다.
        if x % i == 0:
            return False
    return True
'''
다수의 소수 판별
• 하나의 수에 대해서 소수인지 아닌지 판별하는 방법을 알아보았습니다.
• 하지만 특정한 수의 범위 안에 존재하는 모든 소수를 찾아야 할 때는 어떻게 할까요?
• 에라토스테네스의 체 알고리즘을 사용할 수 있습니다.

다수의 자연수에 대하여 소수 여부를 판별할 때 사용하는 대표적인 알고리즘입니다.
• 에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾을 때 사용할 수 있습니다.
• 에라토스테네스의 체 알고리즘의 구체적인 동작 과정은 다음과 같습니다.
1. 2부터 N까지의 모든 자연수를 나열한다.
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
3. 남은 수 중에서 i의 배수를 모두 제거한다 (i는 제거하지 않는다).
4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.

-> 중간값의 제곱근까지만

 
range(n): 0부터 n-1까지의 숫자를 생성합니다.
range(start, stop): start부터 stop-1까지의 숫자를 생성합니다.
range(start, stop, step): start부터 stop-1까지의 숫자를 step 간격으로 생성합니다.

에라토스테네스의 체 알고리즘 성능 분석
• 에라토스테네스의 체 알고리즘의 시간 복잡도는 사실상 선형 시간에 가까울 정도로 매우 빠릅니다.
• 시간 복잡도는 O(NloglogN)입니다.
• 에라토스테네스의 체 알고리즘은 다수의 소수를 찾아야 하는 문제에서 효과적으로 사용될 수 있습니다.
• 하지만 각 자연수에 대한 소수 여부를 저장해야 하므로 메모리가 많이 필요합니다.
• 10억이 소수인지 아닌지 판별해야 할 때 에라토스테네스의 체를 사용할 수 없다. 효율적이지 않다.
'''

def get_prime_numbers():
    n = 1000 # 2부터 ~ 1000까지
    middle = (1000//2)^2
    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화 (0과 1은 제외)
    for i in range(2, middle+1):
        if array[i] == True: # i가 소수인 경우 (또는 남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            multiple = 2 # 2~3,4등 배수 지우기 위한 초기값
            while i * multiple <= n:
                array[i * multiple] = False
                multiple += 1
    # 모든 소수 출력
    for i in range(2, n+1):
        if array[i]:
            print(i, end=' ')

print(get_prime_numbers())


'''
투 포인터 (Two Pointers)
• 투 포인터 알고리즘은 리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리하는 알고리즘을 의미합니다.
• 흔히 2, 3, 4, 5, 6, 7번 학생을 지목해야 할 때 간단히 2번부텅 7번까지의 학생'이라고 부르곤 합니다.
• 리스트에 담긴 데이터에 순차적으로 접근해야 할 때는 시작점과 끝점 2개의 점으로 접근할 데이터의 범위를 표현할 수 있습니다.

특정한 합을 가지는 부분 연속 수열 찾기: 문제 설명
• N개의 자연수로 구성된 수열이 있습니다.
• 합이 M인 부분 연속 수열의 개수를 구해보세요.
• 수행 시간 제한은 O(N)입니다.

토 포인터를 활용하여 다음과 같은 알고리즘으로 문제를 해결할 수 있습니다.

1. 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스(O)를 가리키도록 한다.
2. 현재 부분 합이 M과 같다면, 카운트한다.
3. 현재 부분 합이 M보다 작다면, end를 1 증가시킨다. => 부분합 증가 의미
4. 현재 부분 합이 M보다 크거나 같다면, start를 1 증가시킨다. -> 부분합 감소 의미 
5. 모든 경우를 확인할 때까지 2번, 3번, 4번까지의 과정을 반복한다.
'''
# 데이터의 개수 N, 찾고자 하는 부분합 M, N개의 수열 데이터 data

def find_continuous_sequence(num, sum, data):
    count = 0
    interval_sum = 0
    end = 0
    # start를 차례대로 증가시키며 반복
    for start in range(num):
        # end를 가능한 만큼 이동시키기
        while interval_sum < sum and end < num: # 부분합 구하기
            interval_sum += data[end]
            end += 1
        # 부분합결과가 M일 때 카운트 증가
        if interval_sum == sum:
            count += 1
        interval_sum -= data[start]
    return count

'''
시작점(start)을 한 칸 앞으로 이동시키면서, 이동한 시작점의 값을 부분합(interval_sum)에서 빼는 역할을 합니다.  
투 포인터 알고리즘에서는 시작점(start)과 끝점(end) 두 개의 포인터를 이용하여 부분합을 계산합니다. 
부분합이 목표값(M)보다 크거나 같을 경우, 시작점을 한 칸 앞으로 이동시키면서 부분합에서 시작점의 값을 빼는 작업을 수행합니다. 
이렇게 함으로써 부분합을 줄이고, 다시 목표값과 비교하는 과정을 반복합니다.  
따라서 interval_sum -= data[start]는 시작점을 앞으로 이동시키면서 부분합을 조정하는 데 사용됩니다.
'''

'''
구간 함 (Interval Sum)
• 구간 합 문제: 연속적으로 나열된 N개의 수가 있을 때 특정 구간의 모든 수를 합한 값을 계산하는 문제
• 예를 들어 5개의 데이터로 구성된 수열 {10, 20, 30, 40, 50}이 있다고 가정합시다.
• 두 번째 수부터 네 번째 수까지의 합은 20+ 30+ 40= 90입니다.

N개의 정수로 구성된 수열이 있습니다.
• M개의 쿼리(Query) 정보가 주어집니다.
• 각 쿼리는 Left와 Right으로 구성됩니다.
• 각 쿼리에 대하여 [Left, Right] 구간에 포함된 데이터들의 합을 출력해야 합니다.
• 수행 시간 제한은 O(N + M)입니다.

구간 합 빠르게 계산하기: 문제 해결 아이디어
• 접두사 합(Prefix Sum): 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해 놓은 것
• 접두사 합을 활용한 알고리즘은 다음과 같습니다.
• N개의 수 위치 각각에 대하여 접두사 합을 계산하여 P에 저장합니다. -> 캐시처럼 사용
• 매 M개의 리 정보를 확인할 때 구간 합은 P[Right]-P[Left - 1]입니다.

1) Left = 1, Right = 3
    P[3] - P[0] = 60

2) Left = 2, Right = 5
    P[5] - P[1] = 140

3） Left = 3, Right = 4
    P[4] - P[2] = 70
'''
def prefix_sum():
    # 데이터의 개수 N과 데이터 입력받기
    n = 5
    data = [10, 20, 30, 40, 50]
    # 접두사 합(Prefix Sum) 배열 계산
    sum_value = 0
    prefix_sum = [0]
    for i in data:
        sum_value += i
        prefix_sum.append(sum_value)

    # 구간 합 계산(세 번째 수부터 네 번째 수까지)
    left = 3
    right = 4
    result = prefix_sum[right] - prefix_sum[left - 1] # 70
    return result
print(prefix_sum())
