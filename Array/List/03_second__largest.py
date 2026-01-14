# In given array find second largest element if not print -1

arr = [1,12,34,45,23,67,89,5]

class Solution:

    def secondLargest(self, arr):

        largest = float("-inf")
        s_largest = float("-inf")

        for i in range(0,len(arr)):

            if largest < arr[i]:
                s_largest = largest
                largest = arr[i]

            elif s_largest < arr[i]  and largest != arr[i]:
                s_largest = arr[i]
            else:
                if largest == s_largest:
                    s_largest = -1
            
        return s_largest
    
obj = Solution()
print(obj.secondLargest(arr))