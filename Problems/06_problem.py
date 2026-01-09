#  print the factorial of a number

num = 20
result = []

for i in range(1, num+1):
    if num % i == 0:
        result.append(i)

print(result)

#  Time complexity = 0(n)
#  space complexity = 0(k) k would the no. of factors of the number