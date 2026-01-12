# Extraction of digits using loops

n = int(input("Enter a number: "))
num = n
arr = []
while num > 0:
    last_digit = num % 10
    arr.append(last_digit)
    num = num // 10

print("".join(map(str,arr)))


# map(str,arr)  = Convert digits → string for join