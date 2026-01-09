#  check palidrome in integer

n = 123213
num = n
result = 0

while num > 0:
    ld = num % 10
    result = (result * 10) + ld
    num = num // 10

if n == result:
    print("It's palidrome")
else:
    print("It's not palidrome")

