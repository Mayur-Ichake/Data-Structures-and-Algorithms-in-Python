#  problem 6 sovle in the efficient way

num =29
result = []

for i in range(1,num//2 ):
    if num % i == 0:
        result.append(i)

result.append(num)
print(result)

#  time complexity = o(n/2)  almost same o(n)
#  space complexity = 0(k) 