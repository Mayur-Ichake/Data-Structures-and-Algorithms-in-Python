#  check palidrome in string using loop

n = "abmmcba"
op = len(n)
left = 0
right = op-1

while left < right:
    if n[left] != n[right]:
        print("False")
        break
    left += 1
    right -= 1
else:
    print("True")