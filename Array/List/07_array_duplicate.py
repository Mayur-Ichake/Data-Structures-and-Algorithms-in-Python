# find duplicate elements in an array and print the element whose frequency is more than 1

arr = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 9, 4 ]

class Solution:

    def findDuplicates(self, arr):

        freq_map = {}
        duplicates = []
        
        for i in arr:
            if i in freq_map:
                freq_map[i] += 1
            else:
                freq_map[i] = 0
        
        for i in freq_map:
            if freq_map[i] > 0:
                duplicates.append(i)
        return duplicates
        
solution = Solution()
result = solution.findDuplicates(arr)
print(result) 