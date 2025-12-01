#  Frequency map of numbers

num = [1,2,3,4,1,9,1,2,1,2]

freq_map = {}

for i in range(1, len(num)):
    if num[i] in freq_map:
        freq_map[num[i]] += 1
    else:
        freq_map[num[i]] = 1

print(freq_map)

#  TC = 0(n)
#  SC = o(n)
