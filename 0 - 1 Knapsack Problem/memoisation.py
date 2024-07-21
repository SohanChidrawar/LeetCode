class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        
        dp = [[-1]*(W+1) for _ in range(n)]
        # code here
        
        def helper(index,rem_wt):
            #base case
            if index > n-1 or rem_wt == 0:
                return 0
            
            if dp[index][rem_wt] != -1:
                return dp[index][rem_wt]
            #recursive case
            exclude = helper(index+1,rem_wt)
            include = 0
            if wt[index] <= rem_wt:
                include = val[index] + helper(index+1,rem_wt-wt[index])
            dp[index][rem_wt] = max(include,exclude)
            return dp[index][rem_wt]
        return helper(0,W)
