#  Count the number  for e.g 1224 = 4 & 584771 = 6
from math import * 
# we can count log10(n) + 1 to get number of digits
n = 54321265432
print(int(log10(n))+1)

num = n 
count = 0

while num > 0:
    count += 1
    num = num // 10

print(count)

