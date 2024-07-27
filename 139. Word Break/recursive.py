class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        dp = [False]*n 
    
        def check(index):
            #base case
            if index<0:
                return True

            #recursive case
            for word in wordDict:
                if s[index-len(word)+1 : index+1]== word and check(index-len(word)):
                    return True
            return False

        return check(n-1)
