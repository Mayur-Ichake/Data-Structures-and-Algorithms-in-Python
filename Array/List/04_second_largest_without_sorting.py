# find second largest element in an array

arr = [12, 35, 1, 10, 34, 1]

largest = float("-inf")
s_largest = float("-inf")

for i in range(0,len(arr)):
    if largest < arr[i]:
        s_largest = largest
        largest = arr[i]
    elif s_largest < arr[i] and largest != arr[i]:
        s_largest = arr[i]

print([largest,s_largest])
