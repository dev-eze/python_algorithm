types_count = int(input())
types = list(map(int, input()))

def get_hamburger(types):
    max_value = max(types)
    max_index = types.index(max_value)
    # 1235321
    left = types[0:max_index+1]
    right = types[max_index:-1]

    if sorted(left) == left and sorted(right, reverse = True) == right:
        return sum(types)
    else:
        return 0

print(get_hamburger(types))