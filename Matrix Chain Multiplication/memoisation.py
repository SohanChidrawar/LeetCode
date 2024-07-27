class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        dp = [[-1]*N for _ in range(N)]
        def findcost(i,j):
            if i==j:
                return 0
             
            if dp[i][j]!=-1:
                return dp[i][j]
            min_cost = float('inf')
            for k in range(i,j):
                curr_cost = findcost(i,k)+findcost(k+1,j)+arr[i-1]*arr[k]*arr[j]
                min_cost = min(min_cost,curr_cost)
                
            dp[i][j] = min_cost
            return dp[i][j]
                
        return findcost(1,N-1)
