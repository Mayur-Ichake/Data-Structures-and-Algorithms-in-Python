# find largest element in a list

arr = [3, 5, 7, 2, 8, -1, 4]

largest = float("-inf")

for i in range(0,len(arr)):
    if largest < arr[i]:
        largest = arr[i]

print(largest)