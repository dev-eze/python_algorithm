'''
https://leetcode.com/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=leetcode-75
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

nd = [1,2,3,4,5]

def solution(head):
    if not head:
        return []
    str_list = list(map(str, head))
    stack = []
    for i in range(len(head)):
        result.append(str_list[::-1])
    return result

print(solution(head))