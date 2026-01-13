# Reverse words of given string

s = "the sky is blue"

class Solution:
    def reverseWords(self, s: str) -> str:

        # word = s.split()
        # word[::-1]
        # result = " ".join(word)
        result = " ".join(s.split()[::-1])
        return result
        


obj = Solution()

print(obj.reverseWords(s))