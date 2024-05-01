class Solution: 
    def longestPalindromeSubseq(self, s: str) -> int: 
        n = len(s) 
 
        dp = [[0]*n for _ in range(n)] 
 
        #Base case single character palindrome 
        for i in range(n): 
            dp[i][i] = 1 
 
        #Consider all substring with length gretaer than 1 
        for length in range(2,n+1): 
            for i in range(n-length+1): 
                j = i+length-1 
                if s[i] == s[j]: 
                     # If characters match, add 2 to the inner palindrome length 
                    dp[i][j] = 2 + dp[i+1][j-1] 
                else: 
                    # Otherwise, take the maximum of either removing the first or last character 
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1]) 
        # The result is the longest palindromic subsequence between indices 0 and n-1 
        return dp[0][n-1] 
