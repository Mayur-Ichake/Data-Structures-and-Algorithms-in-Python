# check if array is sorted in non-decreasing order

arr = [10, 20, 30, 40, 50]


for i in range(0,len(arr)-1):
    if arr[i] > arr[i + 1]:
        print(False)
        break
else:
    print(True)

