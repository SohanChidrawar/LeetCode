class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        dp = [[0]*n for _ in range(n)]

        for l in range(1,n+1):
            for i in range(n-l+1):
                j = i+l-1
                
                if i == j:
                    dp[i][j] = True
                    count+=1               
                elif s[i]==s[j] and (j==i+1 or dp[i+1]==dp[j-1]):
                    dp[i][j] = True
                    count += 1
                else:
                    dp[i][j]=False
        return count
