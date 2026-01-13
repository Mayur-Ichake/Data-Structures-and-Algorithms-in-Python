# Que.2 not using method

s = "the sky is blue"

class Solution:

    def reverseWords(self, s: str) -> str:

        # result = ""
        # word = ""
        # for char in s:
        #     if char != " ":
        #         word += char
        #     else:
        #         if word:
        #             result = word + " " + result
        #             word = ""
        # if word:
        #     result = word + " " + result
        # return result.strip()

        result = ""
        word = ""

        for char in s:
            if char != " ":     
                word += char              
            else:                        
                result = word + " " + result
                word = ""
        if word:
            result = word + " " + result 
        
        return result.strip()
            
    
obj = Solution()
print(obj.reverseWords(s))