# Check palindrome in string using loop


n = "abmmcba" 
reversed_str = ""
index = len(n) - 1

while index >= 0:
    reversed_str += n[index]
    index -= 1

if n == reversed_str:
    print("It's palindrome")
else:
    print("It's not palindrome")