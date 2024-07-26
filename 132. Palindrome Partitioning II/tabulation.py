class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        palindrome = [[False]*n for _ in range(n)]
        dp = [0]*n

        for l in range(1,n+1):
            for i in range(n-l+1):
                j = i+l-1
                if i==j:
                    palindrome[i][j]=True
                elif(s[i]==s[j] and (j==i+1 or palindrome[i+1][j-1])):
                    palindrome[i][j]=True
                else:
                    palindrome[i][j]=False

        for end in range(n):
            mincuts = end
            for start in range(end+1):
                if palindrome[start][end]:
                    if start == 0:
                        mincuts = 0
                    else:
                        mincuts = min(mincuts, 1+dp[start-1])

            dp[end] = mincuts
        return dp[n-1]
        
