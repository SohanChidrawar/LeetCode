class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1]*n for _ in range(n)]
        def helper(curr,prev):
            #base case
            if curr > n-1:
                return 0

            if dp[curr][prev+1] != -1:
                return dp[curr][prev+1]
              
            #recursive case
            exclude = helper(curr+1, prev)
            include =  0 
            if prev == -1 or nums[curr] > nums[prev]:
                include = 1 + helper(curr+1, curr)
              
            dp[curr][prev+1] = max(exclude,include)
            return dp[curr][prev+1]
          
        return helper(0,-1)
