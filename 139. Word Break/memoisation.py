class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        dp = [-1]*n 
    
        def check(index):
            #base case
            if index<0:
                return True

            if dp[index]!=-1:
                return dp[index]
            #recursive case
            for word in wordDict:
                if s[index-len(word)+1 : index+1]== word and check(index-len(word)):
                    dp[index] = True
                    return dp[index]
            dp[index] = False
            return dp[index]

        return check(n-1)
        
