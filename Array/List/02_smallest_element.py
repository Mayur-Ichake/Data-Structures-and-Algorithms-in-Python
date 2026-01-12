# find the smallest element in a list

arr = [3, 5, 7, 2, 8, -1, 4]

smallest = float("inf")

for i in range(0,len(arr)):
    if smallest > arr[i]:
        smallest = arr[i]

print(smallest)

# find second largest element in an array

arr = [3, 5, 7, 2, 8, -1, 4]

smallest = float("inf")
s_smallest = float("inf")

for i in range(0,len(arr)):
    if smallest > arr[i]:
        s_smallest = smallest
        smallest = arr[i]
    elif s_smallest > arr[i] and smallest != arr[i]:
        s_smallest = arr[i]

print(s_smallest)