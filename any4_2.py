dic = {}
for i in range(n):
    dic[i] = [eat[i], hot[i]]

result = 0
for i in range(n):
    if hot[i] > eat[i]:
        result += hot[i]

total_eat_time = sum(eat)
final_result = total_eat_time - re