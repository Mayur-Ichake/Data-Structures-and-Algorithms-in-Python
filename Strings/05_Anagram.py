# check 2 string are anagram or not

s1 = "mayur"
s2 = "ruyam"

class Solution:

    def isAnagram(self, st:str, s2:str) -> bool:
        
        if len(s1) != len(s2):
            return False
        
        freq = {}

        for i in s1:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for ch in s2:
            if ch not in freq:
                return False
            freq[ch] -= 1
            if freq[ch] < 0:
                return False

        return True

obj = Solution()
print(obj.isAnagram(s1, s2))