#  Armstrong Number Checker

n = 153

num = n
km = len(str(n))
total = 0

while num > 0:
    ld = num % 10
    total = total + (ld ** km)
    num = num // 10

print(total == n)
