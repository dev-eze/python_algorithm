'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII.
Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Conroman_stringaints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I는 V(5)와 X(10) 앞에 올 때 4와 9가 됩니다.
X는 L(50)과 C(100) 앞에 올 때 40과 90이 됩니다.
C는 D(500)과 M(1000) 앞에 올 때 400과 900이 됩니다.

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
'''
roman_string1, roman_string2, roman_string3 = 'III', 'LVIII', 'MCMXCIV'
def replace_roman_to_int(roman_stringing):
    romans_dict = dict(
        I = 1,
        V = 5,
        X = 10,
        L = 50,
        C = 100,
        D = 500,
        M = 1000
    )

    specials = dict(
        IV = 4,
        IX = 9,
        XL = 40,
        XC = 90,
        CD = 400,
        CM = 900
    )
    roman_stringing_list = list(roman_stringing)
    int_result = []
    for char in roman_stringing_list:
        if char in romans_dict.keys():
            int_result.append(romans_dict[char])
    return sum(int_result)


#print(replace_roman_to_int(roman_string1))
#print(replace_roman_to_int(roman_string2))
print(replace_roman_to_int(roman_string3))


def replace_roman_to_int2(roman_string):
    romans_dict = dict(
        I=1,
        V=5,
        X=10,
        L=50,
        C=100,
        D=500,
        M=1000
    )

    special_dict = dict(
        IV=4,
        IX=9,
        XL=40,
        XC=90,
        CD=400,
        CM=900
    )

    int_result = []
    '''
    I는 V(5)와 X(10) 앞에 올 때 4와 9.
    X는 L(50)과 C(100) 앞에 올 때 40과 90.
    C는 D(500)과 M(1000) 앞에 올 때 400과 900.
    '''

    i = 0
    while i < len(roman_string):
        if i < len(roman_string) - 1 and ''.join(roman_string[i:i+2]) in special_dict:
            int_result.append(special_dict[''.join(roman_string[i:i+2])])
            i += 2
        elif roman_string[i] in romans_dict:
            int_result.append(romans_dict[roman_string[i]])
            i += 1
        else:
            i += 1

    return sum(int_result)

print(replace_roman_to_int2(roman_string1))
print(replace_roman_to_int2(roman_string2))
print(replace_roman_to_int2(roman_string3))