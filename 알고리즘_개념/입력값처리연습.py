user_input = input("Enter something: ")
print(user_input)


# 정수 입력받기
integer_input = int(input("Enter an integer: "))

# 실수 입력받기
float_input = float(input("Enter a float: "))


# 공백으로 구분된 문자열을 입력받아 문자 리스트로 변환
string_list = input("Enter strings separated by space: ").split()

# 공백으로 구분된 숫자를 입력받아 정수 리스트로 변환
integer_list = list(map(int, input("Enter numbers separated by space: ").split()))


#여러 줄에 걸쳐 입력을 받아 2차원 리스트를 생성, 행렬을 입력받는 경우
rows = int(input("Enter number of rows: "))
matrix = [list(map(int, input(f"Enter row {i+1} values separated by space: ").split())) for i in range(rows)]

#사전(Dictionary) 입력받기
#키와 값을 가진 입력을 사전으로 변환,  콜론(:)을 사용하여 키와 값을 구분하는 입력을 받는 경우
dict_input = dict(item.split(":") for item in input("Enter key:value pairs separated by space: ").split())


# 공백으로 구분된 숫자를 입력받아 튜플로 변환
integer_tuple = tuple(map(int, input("Enter numbers separated by space: ").split()))

#튜플 입력받기
# 공백으로 구분된 숫자를 입력받아 튜플로 변환
integer_tuple = tuple(map(int, input("Enter numbers separated by space: ").split()))

'''
튜플 (Tuple)
튜플은 파이썬의 기본 데이터 구조 중 하나로, 순서가 있지만 변경 불가능한(immutable) 컬렉션입니다. 즉, 튜플에 한 번 저장된 데이터는 수정, 추가, 삭제할 수 없습니다. 튜플은 괄호 ()를 사용하여 생성하며, 각 요소는 쉼표로 구분됩니다. 튜플은 다양한 타입의 데이터를 저장할 수 있으며, 다른 컬렉션 타입(리스트, 딕셔너리 등)과 함께 사용될 때 유용하게 사용됩니다.
튜플의 주요 사용 사례 중 하나는 함수에서 여러 값을 반환할 때입니다. 함수는 하나의 튜플을 반환하며, 이 튜플에는 여러 값이 포함될 수 있습니다.
'''
my_tuple = (1, "Hello", 3.14)
print(my_tuple[1])  # 출력: Hello

'''
해시테이블 (Hashtable)
해시테이블은 키-값 쌍으로 데이터를 저장하는 데이터 구조로, 각 키는 해시 함수를 통해 고유한 인덱스로 변환됩니다. 이 인덱스는 해당 키-값 쌍이 저장될 배열의 위치를 결정합니다. 해시테이블의 주요 장점은 평균적으로 
O(1)의 시간 복잡도로 데이터를 검색, 삽입, 삭제할 수 있다는 점입니다.
파이썬에서는 딕셔너리(Dictionary) 타입이 해시테이블의 구현을 제공합니다. 딕셔너리는 중괄호 {}를 사용하여 생성하며, 키-값 쌍은 콜론 :으로 구분됩니다.
'''
my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])  # 출력: Alice

'''
행렬 (Matrix)
행렬은 수학에서 행과 열로 구성된 직사각형 배열을 의미합니다. 컴퓨터 프로그래밍에서 행렬은 주로 숫자를 이차원 배열 형태로 저장하는 데 사용됩니다. 행렬은 수학적 연산, 공학적 계산, 컴퓨터 그래픽스, 기계 학습 등 다양한 분야에서 중요한 역할을 합니다.

파이썬에서는 리스트의 리스트를 사용하여 행렬을 표현할 수 있습니다. 각 내부 리스트는 행렬의 한 행을 나타내며, 리스트의 각 요소는 해당 행의 열 값을 나타냅니다.
더 고급 행렬 연산을 위해서는 NumPy와 같은 수학 라이브러리를 사용할 수 있습니다. NumPy는 효율적인 행렬 연산을 위한 다양한 함수와 메소드를 제공합니다.

이러한 데이터 구조들은 파이썬 프로그래밍의 기본이며, 알고리즘과 데이터 처리에서 중요한 역할을 합니다.
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # 출력: 6, 두 번째 행의 세 번째 열

# 리스트 컴프리헨션 (List Comprehension)
# [expression for item in iterable if condition]
'''
리스트 컴프리헨션은 기존 리스트에서 새로운 리스트를 생성하는 간결하고 효율적인 방법을 제공.
리스트 컴프리헨션(List Comprehension)은 파이썬에서 리스트를 생성하기 위한 간결하고 효율적인 방법입니다. 기존의 리스트나 다른 순회 가능한(iterable) 객체를 기반으로 새로운 리스트를 만들 때, for문과 if문을 사용하는 전통적인 방법보다 훨씬 읽기 쉽고 코드를 짧게 작성할 수 있게 해줍니다.

expression: 새 리스트의 각 요소에 대한 표현식입니다. 여기에는 변수 item을 사용할 수 있으며, 이 변수는 iterable에서 가져온 각 요소에 대응됩니다.
item: iterable에서 순차적으로 가져오는 각 요소를 나타내는 변수입니다.
iterable: 순회 가능한 데이터 구조(예: 리스트, 튜플, 문자열 등)입니다. for item in iterable 구문을 통해 이 구조의 각 요소에 접근합니다.
condition: 선택적으로 사용할 수 있는 조건문입니다. 이 조건을 만족하는 요소에 대해서만 expression이 평가되어 새 리스트에 추가됩니다.
'''
# 0부터 9까지의 수 중에서 짝수만 포함하는 리스트 생성
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # 출력: [0, 2, 4, 6, 8]

# 0부터 4까지의 제곱을 요소로 하는 리스트 생성
squares = [x**2 for x in range(5)]
print(squares)  # 출력: [0, 1, 4, 9, 16]

# 예제 3: 문자열 리스트에서 특정 글자를 포함하는 요소만 선택
words = ["apple", "banana", "cherry", "date"]
a_words = [word for word in words if "a" in word]
print(a_words)  # 출력: ['apple', 'banana', 'date']

'''

''.join(result) 코드는 파이썬에서 문자열 리스트 result를 하나의 문자열로 결합하는 데 사용됩니다. 이 메서드는 문자열의 join() 메서드를 사용하며, 리스트의 모든 요소를 하나의 문자열로 결합할 때 사이에 삽입될 문자열을 지정합니다.

여기서 '' (빈 문자열)은 결합될 문자 사이에 아무것도 삽입하지 않겠다는 것을 의미합니다. 즉, 리스트의 모든 요소를 그 사이에 아무 문자도 없이 연결하겠다는 뜻입니다.

예제
python
Copy code
result = ['H', 'e', 'l', 'l', 'o']
joined_string = ''.join(result)
print(joined_string)
이 코드의 출력은 Hello입니다. join() 메서드는 리스트 result의 모든 요소를 순회하며, 각 요소 사이에 빈 문자열 ''을 삽입하여 결합합니다. 결과적으로, 이 요소들은 모두 연결되어 하나의 문자열을 형성합니다.

join() 메서드는 문자열 리스트를 하나의 문자열로 효율적으로 결합하고자 할 때 자주 사용됩니다. 특히, 파일 경로를 구성하거나, 네트워크 요청의 파라미터를 결합하거나, 간단히 리스트의 요소들을 출력 형태로 변환할 때 유용합니다.

추가 예제: 다른 구분자 사용
join() 메서드에는 빈 문자열 이외에도 다른 문자열을 구분자로 사용할 수 있습니다. 예를 들어, 각 문자 사이에 쉼표와 공백을 삽입하려면 다음과 같이 작성할 수 있습니다:

python
Copy code
result = ['Hello', 'world', '!']
joined_string = ', '.join(result)
print(joined_string)
이 경우의 출력은 Hello, world, !입니다. 여기서 ', ' 문자열이 각 리스트 요소 사이에 삽입됩니다.
'''
result = ['H', 'e', 'l', 'l', 'o']
joined_string = ''.join(result)
print(joined_string)

result = ['Hello', 'world', '!']
joined_string = ', '.join(result)
print(joined_string)

'''
모듈로 연산
모듈로 10^9 + 7로 반환
문제에서 매직페어의 총 개수가 매우 클 수 있기 때문에, 결과를 10^9 + 7로 나눈 나머지를 반환하라고 합니다. 
이는 대규모 수를 다룰 때 흔히 사용되는 기법으로, 계산 결과를 일정 범위 내로 제한하여 오버플로우를 방지하고, 수를 관리하기 쉽게 만듭니다. 
10^9 + 7은 큰 소수(prime number)로, 모듈로 연산에서 자주 사용됩니다.
'''

'''
'''


def reverse_number(x):
    return int(str(x)[::-1])


def count_magic_pairs(numbers):
    MOD = 10 ** 9 + 7
    diffs = [num - reverse_number(num) for num in numbers]
    count = 0
    freq = {}

    for diff in diffs:
        if diff in freq:
            count = (count + freq[diff]) % MOD
        freq[diff] = freq.get(diff, 0) + 1

    return count


# 예시 사용
numbers = [42, 97, 13, 24, 1, 76]
print(count_magic_pairs(numbers))
