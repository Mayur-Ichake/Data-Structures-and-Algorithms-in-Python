'''You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

 
Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

Example 2:

Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".'''

num = "42034"
n = len(num)
class Solution:

    def LargestOddNumber(self, num: str) -> str:
        for i in range(n-1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""
obj = Solution()
obj.LargestOddNumber(num)
print(obj.LargestOddNumber(num))
