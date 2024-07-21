class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        
        def helper(index,rem_wt):
            #base case
            if index > n-1 or rem_wt == 0:
                return 0
    
            #recursive case
            exclude = helper(index+1,rem_wt)
            include = 0
            if wt[index] <= rem_wt:
                include = val[index] + helper(index+1,rem_wt-wt[index])
            return(max(include,exclude))
        return helper(0,W)
