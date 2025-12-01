# Extraction of digits using loops

n = int(input("Enter a number: "))
num = n
km = []
while num > 0:
    digit = num % 10
    km.append(digit)
    num = num // 10
# print(km)
print("".join(map(str,km)))

# map(str,km)  = Convert digits → string for join