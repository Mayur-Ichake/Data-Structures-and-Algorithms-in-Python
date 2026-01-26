'''Given an array arr[] of size n, the task is to find all the Leaders in the array. 
An element is a Leader if it is greater than or equal to all the elements to its right side.

Note: The rightmost element is always a leader.

Examples:

Input: arr[] = [16, 17, 4, 3, 5, 2]
Output: [17 5 2]
Explanation: 17 is greater than all the elements to its right i.e., [4, 3, 5, 2], therefore 17 is a leader.
5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.

Input: arr[] = [1, 2, 3, 4, 5, 2]
Output: [5 2]
Explanation: 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader.
2 has no element to its right, therefore 2 is a leader.'''

arr = [16,17,4,3,5,2,1,34,11]

n = len(arr)
temp = []
'''
for i in range(0,n):
    for j in range(i+1,n):
        if arr[i] < arr[j]:
            break
    else:
        temp.append(arr[i])

print(" ".join(map(str,temp)))'''

max_value = arr[-1]
temp.append(max_value)

for i in range(n-2,-1,-1):
    if arr[i] >= max_value:
        max_value = arr[i]
        temp.append(max_value)

temp.reverse()
print(" ".join(map(str,temp)))

