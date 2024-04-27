'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''
strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]

def longest_common_prefix(strs):
    if not strs:
        return ""

    common_prefix = []
    for each in zip(*strs):
        if len(set(each)) == 1: # 같은 인덱스가 모두 동일한 요소인경우 set 길이 1개
            common_prefix.append(each[0])
        else:
            break
    return ''.join(common_prefix) if len(common_prefix) > 0 else ""

print(longest_common_prefix(strs1))
print(longest_common_prefix(strs2))
