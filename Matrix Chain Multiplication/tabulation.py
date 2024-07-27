class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        dp = [[0]*N for _ in range(N)]
        
        for l in range(1,N):
            for i in range(N-l+1):
                j = i+l-1
                
                if i==j:
                    dp[i][j] == 0
                    
                else:
                    dp[i][j] = float('inf')
                    for k in range(i,j):
                        dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+arr[i-1]*arr[k]*arr[j])
         
        return dp[1][N-1]
