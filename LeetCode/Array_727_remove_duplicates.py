from collections import Counter



nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 7]
def removeDuplicates(nums):
    if not nums:
        return 0

    counter = Counter(nums)
    result = 0

    for each in counter.items():
        if each[1] == 1:
            result += 1
    return result


def removeDuplicates2(nums):
    if not nums:
        return 0

    counter = Counter(nums)
    result = 0

    result += sum(1 for each in counter.items() if each[1] == 1)
    return result

print(removeDuplicates(nums))
print(removeDuplicates2(nums))
