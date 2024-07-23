class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        prev = [0]*(m+1)
        curr = [0]*(m+1)

        # for i in range(n+1):
        #     dp[i][0] = i

        for j in range(m+1):
            prev[j] = j
        

        for i in range(1,n+1):
            curr[0] = i
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    replace = 1 + prev[j-1]
                    delete = 1 + prev[j]
                    insert = 1 + curr[j-1]
                    curr[j] = min(replace,delete,insert)
            prev = curr[:]
        return prev[m]
        
