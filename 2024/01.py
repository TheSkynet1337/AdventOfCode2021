from collections import Counter

input = list(map(int, open('01.txt', 'r').read().split()))
print('Part 1:', sum([abs(pair[0] - pair[1])
                      for pair in zip(sorted(input[::2]), sorted(input[1::2]))]))
right_dict = Counter(input[1::2])
print('Part 2:', sum([left_num * input[1::2].count(left_num)
                      for left_num in input[::2]]))
