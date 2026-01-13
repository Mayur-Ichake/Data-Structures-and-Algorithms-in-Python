# find duplicated from sorted array and remove them in place

arr = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6]
 
'''freq = {}

for i in range(0,len(arr)):
    freq[arr[i]] = 0   # 1,2,3,4,5,6

j = 0

for i in freq:
    arr[j] = i
    j +=1

print(arr)
print(j)'''

class Solution(object):
    def removeDuplicates(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        freq = {}

        for i in range(0,len(arr)):
            freq[arr[i]] = 0

        j = 0 

        for k in freq:
            arr[j] = k
            j += 1

        return arr , j

obj = Solution()
print(obj.removeDuplicates(arr))