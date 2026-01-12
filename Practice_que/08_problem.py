#  problem 6 sovle in the optimal solution 
from math import sqrt
num = 20
result = []

for i in range(1, int(sqrt(num))+1):
    if num % i == 0:
        result.append(i)
        if num// i != i:
            result.append(num//i)

result.sort()   # TC = 0(nlogn)
print(result)

#  time complexity = 0(sprt of n) + 0(nlogn)
#  space complexity = 0(k)