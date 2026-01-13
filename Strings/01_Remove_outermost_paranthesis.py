# Remove the outermost paranthesis

s = "(()())((()))(())"

class Solution:
    def removeoutermostparanthesis(self, s: str) -> str:
        result = ""
        count = 0

        for i in s:
            if i == "(":
                if count > 0:
                    result += i
                count += 1
            else:
                count -= 1
                if count > 0:
                    result += i
        return result 
    
obj = Solution()
print(obj.removeoutermostparanthesis(s))