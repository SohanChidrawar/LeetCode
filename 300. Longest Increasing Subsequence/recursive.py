class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(curr,prev):
            if curr > n-1:
                return 0

            #recursive case
            exclude = helper(curr+1, prev)
            include =  0 
            if prev == -1 or nums[curr] > nums[prev]:
                include = 1 + helper(curr+1, curr)
            return max(exclude,include)

        return helper(0,-1)
