from collections import Counter
'''
import java.util.HashMap;
public class Main {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 1, 2, 3, 1, 2, 3};
        System.out.println(solution(nums));
    }

    public static int solution(int[] data) {
        if (data.length == 0) return 0;

        // HashMap을 사용하여 각 숫자의 등장 횟수를 저장
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : data) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        int count = 0;
        for (int value : map.values()) {
            if (value == 1) {
                count++;
            }
        }
        return count;
    }
}

'''



nums = [1,1,2]
def removeDuplicates(nums):
    if not nums:
        return 0

    counter = Counter(nums)
    count = 0

    for each in counter.items():
        if each[1] == 1:
            count += 1 # result += sum(1 for each in counter.items() if each[1] == 1)
    result = len(counter.keys())
    return result


def removeDuplicates2(nums):
    if not nums:
        return 0

    dict = {}
    result = 0

    for each in nums:
        dict[each] = dict.get(each, 0) + 1

    result = sum(1 for each in dict.items() if each[1] == 1)
    return result


def count_prime(nums):
    if not nums:
        return 0

    freq_map = {}

    for each in nums:
        freq_map[each] = freq_map.get(each, 0) + 1

    result = [key for key, value in freq_map.items() if value == 1]
    return list(map(int, freq_map.keys()))

print(count_prime(nums))
