# Given a string s, reverse the string without reversing its individual words. Words are separated by dots(.).

s = "..i..like.this.progrm..very.much.."

class Solution:

    def revserWords(self, s):

        # Step 1: split by dot
        parts = s.split('.')
        
        # Step 2: remove empty strings
        words = []
        for word in parts:
            if word != "":
                words.append(word)
        
        # Step 3: reverse words
        words.reverse()
        
        # Step 4: join with single dot
        return ".".join(words)
    
solution = Solution()
print(solution.revserWords(s)) 