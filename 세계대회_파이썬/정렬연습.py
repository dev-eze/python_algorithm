n = int(input())
words = [input() for i in range(n)]

sorted_words = sorted(words)

for each in sorted_words:
    print(''.join(each), end='\n')